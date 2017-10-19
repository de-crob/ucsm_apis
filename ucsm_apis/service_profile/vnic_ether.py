"""
This module intends on creating higher level api calls for establishing an
 Vnic Ether
"""
from ucsmsdk.ucsexception import UcsOperationError

def vnic_ether_create(handle, name, ls_server_dn, adaptor_profile_name=None,
					  addr="derived", admin_cdn_name=None, 
					  admin_host_port="ANY", admin_vcon="any", 
					  cdn_prop_in_sync=None, cdn_source=None, 
					  ident_pool_name=None, mtu=None, 
					  nw_ctrl_policy_name=None, nw_templ_name=None, order=None,
					  pin_to_group_name=None, qos_policy_name=None, 
					  stats_policy_name=None, switch_id=None, **kwargs):
	"""
	create a vnic ethernet profile
	
	Args:
		handle (UcsHandle)
		name (string):
		adaptor_profile_name (string):
		addr (): 
		admin_cdn_name (string):
		admin_host_port (string): '1' or '2' or 'ANY' or 'NONE'
		admin_vcon (string): '1' or '2' or '3' or '4' or 'any'
		cdn_prop_in_sync (string): 'yes' or 'no' or 'true' or 'false'
		cdn_source (string): 'user-defined" or "vnic-name"
		ident_pool_name (string):
		mtu (string):
		nw_ctrl_policy_name (string):
		nw_templ_name(string):
		order (string):
		pin_to_group_name (string):
		qos_policy_name (string):
		stats_policy_name (string):		
		switch_id (string): 'A' or 'B' or 'A-B' or 'B-A' or 'NONE'
		
	Returns:
		VnicEther: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.vnic.VnicEther import VnicEther
	
	obj = handle.query_dn(ls_server_dn)
	if not obj:
		raise UcsOperationError("vnic_ether_create", "Org '%s' does not \
								  exist" % ls_server_dn)
								  
	mo = VnicEther(parent_mo_or_dn=obj, name=name, 
				   adaptor_profile_name=adaptor_profile_name, addr=addr, 
				   admin_cdn_name=admin_cdn_name, 
				   admin_host_port=admin_host_port, admin_vcon=admin_vcon,
				   cdn_prop_in_sync=cdn_prop_in_sync, cdn_source=cdn_source,
				   ident_pool_name=ident_pool_name, mtu=mtu, 
				   nw_ctrl_policy_name=nw_ctrl_policy_name, 
				   nw_templ_name=nw_templ_name, order=order, 
				   pin_to_group_name=pin_to_group_name, 
				   qos_policy_name=qos_policy_name, 
				   stats_policy_name=stats_policy_name, switch_id=switch_id)
				   
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present=True)
	handle.commit()
	return mo
	
def vnic_ether_get(handle, name, ls_server_dn, caller="vnic_ether_get"):
	"""
	gets ls server

	Args:
		handle(UcsHandle)
		name (string): ls server name
		org_dn (string): location to place ls server
		caller (string): caller method name
		
	Returns:
		LsServer: managed object
		
	Raises:
		UcsOperationError: if VnicEther is not present
		
	Example:
		
	"""

	dn = ls_server_dn + "/ether-" + name
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "VnicEther '%s' does not exist" % dn)
	return mo
		
def vnic_ether_exists(handle, name, ls_server_dn, **kwargs):
	"""
	checks if vnic ether exists
	
	Args:
		handle(UcsHandle)
		name (string): ls server name
		org_dn (string): location to place ls server
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, VnicEther MO/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = vnic_ether_get(handle=handle, name=name, ls_server_dn=ls_server_dn, 
						   caller="vnic_ether_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def vnic_ether_modify(handle, name, ls_server_dn, **kwargs):
	"""
	modifies vnic ether
	
	Args:
		handle (UcsHandle)
		name (string): vnic ether name
		org_dn (string): location to place vnic ether
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		LsServer: managed object
		
	Raises:
		UcsOperationError: if VnicEther is not present
		
	Example:
		
	"""
	
	mo = vnic_ether_get(handle=handle, name=name, ls_server_dn=ls_server_dn, 
					   caller="vnic_ether_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def vnic_ether_delete(handle, name, ls_server_dn):
	"""
	deletes vnic ether
	
	Args:
		handle (UcsHandle)
		name (String): vnic ether name
		ls_server_dn (string): location to place vnic ether
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if VnicEther is not present
		
	Example:
		
	"""
	
	mo = vnic_ether_get(handle=handle, name=name, ls_server_dn=ls_server_dn, 
					   caller="vnic_ether_delete")
	handle.remove_mo(mo)
	handle.commit()
	
def vnic_ether_if_create(handle, name, vnic_ether_dn, default_net=None, 
						 **kwargs):
	"""
	create a vnic ethernet profile
	
	Args:
		handle (UcsHandle)
		name (string):
		vnic_ether_dn (string):
		default_net (string): 'yes' or 'no' or 'true' or 'false'
		**kwargs: Any additional key-value pair of managed object(MO)'s
                  property and value, which are not part of regular args.
                  This should be used for future version compatibility.
		
	Returns:
		VnicEtherIf: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.vnic.VnicEtherIf import VnicEtherIf
	
	obj = handle.query_dn(vnic_ether_dn)
	if not obj:
		raise UcsOperationError("vnic_ether_if_create", "Org '%s' does not \
								  exist" % vnic_ether_dn)
								  
	mo = VnicEtherIf(parent_mo_or_dn=obj, name=name, default_net=default_net)
				   
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present=True)
	handle.commit()
	return mo
	
def vnic_ether_if_get(handle, name, vnic_ether_dn, caller="vnic_ether_if_get"):
	"""
	gets ls server

	Args:
		handle(UcsHandle)
		name (string): vnic ether if name
		vnic_ether_dn (string): location to place vnic ether
		caller (string): caller method name
		
	Returns:
		VnicEtherIf: managed object
		
	Raises:
		UcsOperationError: if VnicEtherIf is not present
		
	Example:
		
	"""

	dn = vnic_ether_dn + "/if-" + name
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "VnicEtherIf '%s' does not exist" % dn)
	return mo
		
def vnic_ether_if_exists(handle, name, vnic_ether_dn, **kwargs):
	"""
	checks if vnic ether exists
	
	Args:
		handle(UcsHandle)
		name (string): ls server name
		vnic_ether_dn (string): location to place ls server
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, VnicEtherIf MO/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = vnic_ether_if_get(handle=handle, name=name, 
							   vnic_ether_dn=vnic_ether_dn, 
							   caller="vnic_ether_if_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def vnic_ether_if_modify(handle, name, vnic_ether_dn, **kwargs):
	"""
	modifies vnic ether
	
	Args:
		handle (UcsHandle)
		name (string): vnic ether name
		vnic_ether_dn (string): location to place vnic ether
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		VnicEtherIf: managed object
		
	Raises:
		UcsOperationError: if VnicEtherIf is not present
		
	Example:
		
	"""
	
	mo = vnic_ether_if_get(handle=handle, name=name, 
						   vnic_ether_dn=vnic_ether_dn,
						   caller="vnic_ether_if_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def vnic_ether_if_delete(handle, name, vnic_ether_dn):
	"""
	deletes vnic ether
	
	Args:
		handle (UcsHandle)
		name (String): vnic ether name
		vnic_ether_dn (string): location to place vnic ether
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if VnicEtherIf is not present
		
	Example:
		
	"""
	
	mo = vnic_ether_if_get(handle=handle, name=name, 
						   vnic_ether_dn=vnic_ether_dn, 
						   caller="vnic_ether_if_delete")
	handle.remove_mo(mo)
	handle.commit()
	
