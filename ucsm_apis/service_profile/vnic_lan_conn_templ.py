"""
This module intends on creating higher level api calls for establishing an
 VnicLanConnTempl
"""

from ucsmsdk.ucsexception import UcsOperationError

def vnic_lan_conn_templ_create(handle, name, obj_dn="org-root", 
							   admin_cdn_name=None, cdn_source=None, descr=None,
							   ident_pool_name=None, mtu=None, 
							   nw_ctrl_policy_name=None, 
							   peer_redundancy_templ_name=None, 
							   pin_to_group_name=None, policy_owner=None,
							   qos_policy_name=None, redundancy_pair_type=None,
							   stats_policy_name=None, switch_id=None, 
							   target=None ,templ_type=None, **kwargs):
	"""
	create the vnic lann conn templ 
	
	Args:
		handle (UcsHandle)
		admin_cdn_name (string):
		cdn_source (string): 'user-defined' or 'vnicname'
		descr (string):
		ident_pool_name (string):
		mtu (string):
		nw_ctrl_policy_name (string):
		peer_redundancy_templ_name (string):
		pin_to_group_name (string):
		policy_owner (string): 'local' or 'pending-policy' or 'policy'
		qos_policy_name (string):
		redundancy_pair_type (string): 'none' or 'primary' or 'secondary'
		stats_policy_name (string):
		switch_id (string): 'A' or 'B' or 'A-B' or 'B-A'
		target (string):
		templ_type (string): 'initial-template' or 'updating-template'
		**kwargs:
		
	Returns:
		VnicLanConnTempl: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.vnic.VnicLanConnTempl import VnicLanConnTempl
	
	obj = handle.query_dn(obj_dn)
	if not obj:
		raise UcsOperationError("vnic_lan_conn_templ_create", "LsServer '%s' \
								does not exist" % obj_dn)
	
	mo = VnicLanConnTempl(parent_mo_or_dn=obj, name=name, 
						  admin_cdn_name=admin_cdn_name, cdn_source=cdn_source,
						  descr=descr, ident_pool_name=ident_pool_name, 
						  mtu=mtu, nw_ctrl_policy_name=nw_ctrl_policy_name, 
						  peer_redundancy_templ_name=peer_redundancy_templ_name,
						  pin_to_group_name=pin_to_group_name, 
						  policy_owner=policy_owner, 
						  qos_policy_name=qos_policy_name, 
						  redundancy_pair_type=redundancy_pair_type, 
						  stats_policy_name=stats_policy_name, 
						  switch_id=switch_id, target=target, 
						  templ_type=templ_type)	
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present = True)
	handle.commit()
	return mo
	
def vnic_lan_conn_templ_get(handle, name,  obj_dn, 
							caller="vnic_lan_conn_templ_get"):
	"""
	gets vnic lan conn templ
	
	Args:
		handle (UcsHandle)
		name (string):
		obj_dn (string):
		caller (string):
		
	Returns:
		VnicLanConnTempl: managed object
		
	Raises:
		UcsOperationError: if VnicLanConnTempl is not present
		
	Example:
		
	"""
	dn = obj_dn + "/lan-conn-templ-" + name 
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "VnicLanConnTempl '%s' does not exist"\
								% dn)
	return mo
	
def vnic_lan_conn_templ_exists(handle, name, obj_dn, **kwargs):
	"""
	checks if vnic lan conn templ exists
	
	Args:
		handle(UcsHandle)
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, VnicLanConnTempl mo/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = vnic_lan_conn_templ_get(handle=handle, name=name, obj_dn=obj_dn, 
									 caller="vnic_lan_conn_templ_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def vnic_lan_conn_templ_modify(handle, name, ls_server_dn, **kwargs):
	"""
	modifies vnic lan conn templ
	
	Args:
		handle (UcsHandle)
		name (string):
		ls_server_dn (string):
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		VnicLanConnTempl: managed object
		
	Raises:
		UcsOperationError: if VnicLanConnTempl is not present
		
	Example:
		
	"""
	mo = vnic_lan_conn_templ_get(handle=handle, name=name, obj_dn=obj_dn, 
								 caller="vnic_lan_conn_templ_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def vnic_lan_conn_templ_delete(handle, name, ls_server_dn):
	"""
	deletes vnic lan conn templ
	
	Args:
		handle (UcsHandle)
		name (string):
		ls_server_dn (string):
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if LsmaintAckl is not present
		
	Example:
		
	"""
	mo = vnic_lan_conn_templ_get(handle=handle, name=name, obj_dn=obj_dn,
								 caller="lsmaint_ack_delete")
	handle.remove_mo(mo)
	handle.commit()