"""
This module intends on creating higher level api calls for establishing an
 LsPower
"""
from ucsmsdk.ucsexception import UcsOperationError

def ls_power_create(handle, ls_server_dn, state=None, **kwargs):
	"""
	create the ls power
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		state (string): 'admin-down' or 'admin-up' or 'bmc-reset-immediate' or 
						'bmc-reset-wait' or 'cmos-reset-immediate' or 
						'cycle-immediate' or 'cycle-wait' or 
						'diagnostic-interrupt' or 'down' or 
						'hard-reset-immediate' or 'hard-reset-wait' or 
						'ipmi-reset' or 'kvm-reset' or 'soft-shut-down' or 
						'soft-shut-down-only' or 'up'
		**kwargs:
		
	Returns:
		LsPower: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.ls.LsPower import LsPower
	
	obj = handle.query_dn(ls_server_dn)
	if not obj:
		raise UcsOperationError("ls_power_create", "LsServer '%s' does\
								  not exist" % ls_server_dn)
	
	mo = LsPower(parent_mo_or_dn=obj, state=state)	
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present = True)
	handle.commit()
	return mo
	
def ls_power_get(handle, ls_server_dn, caller="ls_power_get"):
	"""
	gets ls power
	
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
	dn = ls_server_dn + "/power"
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "LsPower '%s' does not exist" % dn)
	return mo
	
def ls_power_exists(handle, ls_server_dn, **kwargs):
	"""
	checks if ls power exists
	
	Args:
		handle(UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, LsPower mo/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = ls_power_get(handle=handle, ls_server_dn=ls_server_dn, 
						  caller="ls_power_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def ls_power_modify(handle, ls_server_dn, **kwargs):
	"""
	modifies ls power
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		LsPower: managed object
		
	Raises:
		UcsOperationError: if LsPower is not present
		
	Example:
		
	"""
	mo = ls_power_get(handle=handle, ls_server_dn=ls_server_dn, 
					  caller="ls_power_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def ls_power_delete(handle, ls_server_dn):
	"""
	deletes ls power
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if LsPower is not present
		
	Example:
		
	"""
	mo = ls_power_get(handle=handle, ls_server_dn=ls_server_dn, 
					  caller="ls_power_delete")
	handle.remove_mo(mo)
	handle.commit()