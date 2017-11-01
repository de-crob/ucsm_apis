"""
This module intends on creating higher level api calls for establishing an
 Fabric Vcon
"""
from ucsmsdk.ucsexception import UcsOperationError

def fabric_vcon_create(handle, id, ls_server_dn, fabric='NONE', 
					   inst_type="manual", placement="physical", select="all", 
					   share="shared", transport="ethernet", **kwargs):
	"""
	create fabric vcon
	
	Args:
		handle (UcsHandle)
		id (string): '1' or '2' or '3' or '4'
		ls_server_dn (string):
		fabric (string): 'A' or 'B' or 'any' or 'NONE'
		inst_type (string): 'auto' or 'manual' or 'policy'
		placement (string): 'auto' or 'physical'
		select (string): 'all' or 'assigned-only' or 'dynamic-only' or 
						 'exclude-dynamic' or 'exclude-unassigned' or 
						 'exclude-usnic' or 'unassigned-only' or 'usnic-only'
		share (string): 'different-transport' or 'exclusive-only' or
						'exclusive-preferred' or 'same-transport' or 'shared'
		transport (string): 
		
	Returns:
		FabricVCon: managed object
	
	Raises:
		UcsOperationError: if LsServer is not present
		
	Example:
		
	"""
	
	from ucsmsdk.mometa.fabric.FabricVCon import FabricVCon
	
	obj = handle.query_dn(ls_server_dn)
	if not obj:
		raise UcsOperationError("fabric_vcon_create", "LsServer '%s' does not \
								  exist" % ls_server_dn)
								  
	mo = FabricVCon(parent_mo_or_dn=obj, id=id, fabric=fabric, 
					inst_type=inst_type, placement=placement, select=select, 
					share=share, transport=transport)				   
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present=True)
	handle.commit()
	return mo
	
def fabric_vcon_get(handle, id, ls_server_dn, caller="fabric_vcon_get"):
	"""
	get fabric vcon
	
	Args:
		handle (UcsHandle)
		id (string): 
		ls_server_dn (string):
		caller (string):
				
	Returns:
		FabricVCon: managed object
		
	Raises:
		UcsOperationError: if the FabricVCon is not present
		
	Example:
		
	"""
	dn = ls_server_dn + "/vcon-" + id
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "FabricVCon '%s' does not exist" % dn)
	return mo
	
def fabric_vcon_exists(handle, id, ls_server_dn, **kwargs):
	"""
	checks if fabric vcon exists
	
	Args:
		handle(UcsHandle)
		id (string): ls server name
		ls_server_dn (string): location to place ls server
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, FabricVCon mo/None)
		
	Raises:
		None
		
	Example:
		
	"""
	
	try:
		mo = fabric_vcon_get(handle=handle, id=id, ls_server_dn=ls_server_dn,
							 caller="fabric_vcon_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def fabric_vcon_modify(handle, id, ls_server_dn, **kwargs):
	"""
	modifies fabric vcon
	
	Args:
		handle (UcsHandle)
		id (string):
		ls_server_dn (string):
		**kwargs:
		
	Returns:
		FabricVCon: managed object
		
	Raises:
		UcsOperationError: if FabricVCon is not present
		
	Example:
			
	"""
	mo = fabric_vcon_get(handle=handle, id=id, ls_server_dn=ls_server_dn,
						 caller="fabric_vcon_modify")
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def fabric_vcon_delete(handle, id, ls_server_dn):
	"""
	deletes fabric vcon
	
	Args:
		handle (UcsHandle)
		id (String): ls server name
		ls_server_dn (string): ls server's full name
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if FabricVCon is not present
		
	Example:
		
	"""
	
	mo = fabric_vcon_get(handle=handle, id=id, ls_server_dn=ls_server_dn,
						 caller="fabric_vcon_delete")
	handle.remove_mo()
	handle.commit()