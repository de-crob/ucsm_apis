"""
This module intends on creating higher level api calls for establishing an
 LsServerFsm
"""
from ucsmsdk.ucsexception import UcsOperationError

def lsmaint_ack_create(handle, ls_server_dn, admin_state=None, auto_delete=None,
					   descr=None, policy_owner=None, scheduler=None, **kwargs):
	"""
	create the lsmaint ack
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		admin_state (string): 'trigger' or 'triggered' or 'trigger-immediate' or
							  'user-ack' or 'user-discard'
		auto_delete (string): 'yes' or 'no' or 'true' or 'false'
		descr (string):
		policy_owner (string): 'local' or 'pending-policy' or 'policy'
		scheduler (string): 
		**kwargs:
		
	Returns:
		LsmaintAck: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.lsmaint.LsmaintAck import LsmaintAck
	
	obj = handle.query_dn(ls_server_dn)
	if not obj:
		raise UcsOperationError("lsmaint_ack_create", "LsServer '%s' does\
								  not exist" % ls_server_dn)
	
	mo = LsmaintAck(parent_mo_or_dn=obj, admin_state=admin_state, 
					auto_delete=auto_delete, descr=descr, 
					policy_owner=policy_owner, scheduler=scheduler)	
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present = True)
	handle.commit()
	return mo
	
def lsmaint_ack_get(handle, ls_server_dn, caller="lsmaint_ack_get"):
	"""
	gets lsmaint ack
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		caller (string):
		
	Returns:
		LsmaintAck: managed object
		
	Raises:
		UcsOperationError: if LsmaintAck is not present
		
	Example:
		
	"""
	dn = ls_server_dn + "/ack"
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "LsmaintAck '%s' does not exist" % dn)
	return mo
	
def lsmaint_ack_exists(handle, ls_server_dn, **kwargs):
	"""
	checks if lsmaint ack exists
	
	Args:
		handle(UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, LsmaintAck mo/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = lsmaint_ack_get(handle=handle, ls_server_dn=ls_server_dn, 
							 caller="lsmaint_ack_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def lsmaint_ack_modify(handle, ls_server_dn, **kwargs):
	"""
	modifies lsmaint ack
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		LsmaintAck: managed object
		
	Raises:
		UcsOperationError: if LsmaintAck is not present
		
	Example:
		
	"""
	mo = lsmaint_ack_get(handle=handle, ls_server_dn=ls_server_dn, 
					     caller="lsmaint_ack_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def lsmaint_ack_delete(handle, ls_server_dn):
	"""
	deletes ls maint ack
	
	Args:
		handle (UcsHandle)
		ls_server_dn (string):
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if LsmaintAckl is not present
		
	Example:
		
	"""
	mo = lsmaint_ack_get(handle=handle, ls_server_dn=ls_server_dn, 
					     caller="lsmaint_ack_delete")
	handle.remove_mo(mo)
	handle.commit()