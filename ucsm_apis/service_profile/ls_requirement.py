"""
This module intends on creating higher level api calls for establishing an
 LsRequirement
"""
from ucsmsdk.ucsexception import UcsOperationError

def ls_requirement_create(handle, ls_server_dn ,name=None, qualifier=None, 
						  restrict_migration=None, **kwargs):
	"""
	create the ls requirement
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		name (string):
		qualifier (string):
		restrict_migration (string):
		**kwargs:
		
	Returns:
		LsRequirement: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.ls.LsRequirement import LsRequirement
	
	obj = handle.query_dn(ls_server_dn)
	if not obj:
		raise UcsOperationError("ls_requirement_create", "LsServer '%s' does\
								  not exist" % ls_server_dn)
	
	mo = LsRequirement(parent_mo_or_dn=obj, name=name, qualifier=qualifier, 
					   restrict_migration=restrict_migration)	
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present = True)
	handle.commit()
	return mo
	
def ls_requirement_get(handle, ls_server_dn, caller="ls_requirement_get"):
	"""
	gets ls requirement
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		caller (string):
		
	Returns:
		LsRequirement: managed object
		
	Raises:
		UcsOperationError: if LsRequirement is not present
		
	Example:
		
	"""
	dn = ls_server_dn + "/pn-req"
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "LsRequirement '%s' does not exist" \
								% dn)
	return mo
	
def ls_requirement_exists(handle, ls_server_dn, **kwargs):
	"""
	checks if ls requirement exists
	
	Args:
		handle(UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, LsRequirement mo/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = ls_requirement_get(handle=handle, ls_server_dn=ls_server_dn, 
								caller="ls_requirement_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def ls_requirement_modify(handle, ls_server_dn, **kwargs):
	"""
	modifies ls requirement
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		LsRequirement: managed object
		
	Raises:
		UcsOperationError: if LsRequirement is not present
		
	Example:
		
	"""
	mo = ls_requirement_get(handle=handle, ls_server_dn=ls_server_dn, 
					   caller="ls_requirement_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def ls_requirement_delete(handle, ls_server_dn):
	"""
	deletes ls server
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if LsRequirement is not present
		
	Example:
		
	"""
	mo = ls_requirement_get(handle=handle, ls_server_dn=ls_server_dn, 
					   caller="ls_requirement_delete")
	handle.remove_mo(mo)
	handle.commit()
	
