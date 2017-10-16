"""
This module intends on creating higher level api calls for establishing an
 LsServerFsm
"""
from ucsmsdk.ucsexception import UcsOperationError

def ls_server_fsm_create(handle, ls_server_dn, **kwargs):
	"""
	create the ls server fsm
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		**kwargs:
		
	Returns:
		LsServerFsm: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.ls.LsServerFsm import LsServerFsm
	
	obj = handle.query_dn(ls_server_dn)
	if not obj:
		raise UcsOperationError("ls_server_fsm_create", "LsServer '%s' does\
								  not exist" % ls_server_dn)
	
	mo = LsServerFsm(parent_mo_or_dn=obj)	
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present = True)
	handle.commit()
	return mo
	
def ls_server_fsm_get(handle, ls_server_dn, caller="ls_server_fsm_get"):
	"""
	gets ls server fsm
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		caller (string):
		
	Returns:
		LsPower: managed object
		
	Raises:
		UcsOperationError: if LsPower is not present
		
	Example:
		
	"""
	dn = ls_server_dn + "/fsm"
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "LsServerFsm '%s' does not exist" % dn)
	return mo
	
def ls_server_fsm_exists(handle, ls_server_dn, **kwargs):
	"""
	checks if ls server fsm exists
	
	Args:
		handle(UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, LsServerFsm mo/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = ls_server_fsm_get(handle=handle, ls_server_dn=ls_server_dn, 
							   caller="ls_power_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def ls_server_fsm_modify(handle, ls_server_dn, **kwargs):
	"""
	modifies ls server fsm
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		LsServerFsm: managed object
		
	Raises:
		UcsOperationError: if LsSeverFsm is not present
		
	Example:
		
	"""
	mo = ls_server_fsm_get(handle=handle, ls_server_dn=ls_server_dn, 
					  caller="ls_server_fsm_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def ls_server_fsm_delete(handle, ls_server_dn):
	"""
	deletes ls server fsm
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if LsServerFsm is not present
		
	Example:
		
	"""
	mo = ls_server_fsm_get(handle=handle, ls_server_dn=ls_server_dn, 
					  caller="ls_server_fsm_delete")
	handle.remove_mo(mo)
	handle.commit()