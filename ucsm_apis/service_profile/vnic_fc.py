"""
This module intends on creating higher level api calls for establishing an
 Vnic Fc
"""
from ucsmsdk.ucsexception import UcsOperationError

def vnic_fc_create(handle, name, ls_server_dn, adaptor_profile_name="",
				   addr="derived", admin_cdn_name="", admin_host_port="ANY", 
				   admin_vcon="any", cdn_prop_in_sync=None, cdn_source=None,
				   ident_pool_name="", max_data_field_size="", 
				   nw_templ_name="", order="", pers_bind="disabled",
				   pers_bind_clear="no", pin_to_group_name="",
				   qos_policy_name="", stats_policy_name="", switch_id="",
				   **kwargs):
	"""
	create a vnic fiber connection profile
	
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
		max_data_field_size (string):
		nw_templ_name (string):
		order (string):
		pers_bind (string): 'enabled' or 'disabled'
		pers_bind_clear (string): 'yes' or 'no' or 'true' or 'false'
		pin_to_group_name (string):
		qos_policy_name (string):
		stats_policy_name (string):		
		switch_id (string): 'A' or 'B' or 'A-B' or 'B-A' or 'NONE'
		
	Returns:
		VnicFc: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.vnic.VnicFc import VnicFc
	
	obj = handle.query_dn(ls_server_dn)
	if not obj:
		raise UcsOperationError("vnic_fc_create", "LsServer '%s' does not \
								  exist" % ls_server_dn)
								  
	mo = VnicFc(parent_mo_or_dn=obj, name=name, 
				adaptor_profile_name=adaptor_profile_name, addr=addr, 
				admin_cdn_name=admin_cdn_name, 
				admin_host_port=admin_host_port, admin_vcon=admin_vcon,
				cdn_prop_in_sync=cdn_prop_in_sync, cdn_source=cdn_source,
				ident_pool_name=ident_pool_name, 
				max_data_field_size=max_data_field_size, 
				nw_templ_name=nw_templ_name, order=order, 
				pers_bind=pers_bind, pers_bind_clear=pers_bind_clear,
				pin_to_group_name=pin_to_group_name, 
				qos_policy_name=qos_policy_name, 
				stats_policy_name=stats_policy_name, switch_id=switch_id)
				   
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present=True)
	handle.commit()
	return mo
	
def vnic_fc_get(handle, name, ls_server_dn, caller="vnic_fc_get"):
	"""
	gets vnic fc

	Args:
		handle(UcsHandle)
		name (string): vnic fc name
		ls_server_dn (string): location to place ls server
		caller (string): caller method name
		
	Returns:
		VnicFc: managed object
		
	Raises:
		UcsOperationError: if VnicFc is not present
		
	Example:
		
	"""

	dn = ls_server_dn + "/fc-" + name
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "VnicFc '%s' does not exist" % dn)
	return mo
		
def vnic_fc_exists(handle, name, ls_server_dn, **kwargs):
	"""
	checks if vnic fc exists
	
	Args:
		handle(UcsHandle)
		name (string): vnic fc name
		ls_server_dn (string): location to place ls server
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, VnicFc MO/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = vnic_fc_get(handle=handle, name=name, ls_server_dn=ls_server_dn, 
						   caller="vnic_fc_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def vnic_fc_modify(handle, name, ls_server_dn, **kwargs):
	"""
	modifies vnic fc
	
	Args:
		handle (UcsHandle)
		name (string): vnic fc name
		ls_server_dn (string): location to place vnic fc
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		VnicFc: managed object
		
	Raises:
		UcsOperationError: if VnicFc is not present
		
	Example:
		
	"""
	
	mo = vnic_fc_get(handle=handle, name=name, ls_server_dn=ls_server_dn, 
					   caller="vnic_fc_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def vnic_fc_delete(handle, name, ls_server_dn):
	"""
	deletes vnic fc
	
	Args:
		handle (UcsHandle)
		name (String): vnic ether name
		ls_server_dn (string): location to place vnic fc
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if VnicFc is not present
		
	Example:
		
	"""
	
	mo = vnic_fc_get(handle=handle, name=name, org_dn=org_dn, 
					   caller="vnic_fc_delete")
	handle.remove_mo(mo)
	handle.commit()
	
def vnic_fc_if_create(handle, name, vnic_fc_dn, **kwargs):
	"""
	create a vnic fc profile
	
	Args:
		handle (UcsHandle)
		name (string):
		vnic_fc_dn (string):
		**kwargs: Any additional key-value pair of managed object(MO)'s
                  property and value, which are not part of regular args.
                  This should be used for future version compatibility.
		
	Returns:
		VnicFcIf: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
		
	Example:
		
	"""
	from ucsmsdk.mometa.vnic.VnicFcIf import VnicFcIf
	
	obj = handle.query_dn(vnic_fc_dn)
	if not obj:
		raise UcsOperationError("vnic_fc_if_create", "Org '%s' does not \
								  exist" % vnic_fc_dn)
								  
	mo = VnicFcIf(parent_mo_or_dn=obj, name=name)
				   
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present=True)
	handle.commit()
	return mo
	
def vnic_fc_if_get(handle, name, vnic_fc_dn, caller="vnic_fc_if_get"):
	"""
	gets ls server

	Args:
		handle(UcsHandle)
		name (string): vnic fc if name
		vnic_fc_dn (string): location to place vnic fc
		caller (string): caller method name
		
	Returns:
		VnicFcIf: managed object
		
	Raises:
		UcsOperationError: if LsServer is not present
		
	Example:
		
	"""

	dn = vnic_fc_dn + "/if-" + name
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "VnicFcIf '%s' does not exist" % dn)
	return mo
		
def vnic_fc_if_exists(handle, name, vnic_fc_dn, **kwargs):
	"""
	checks if vnic fc exists
	
	Args:
		handle(UcsHandle)
		name (string): vnic fc name
		vnic_fc_dn (string): location to place vnic fc
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, VnicFcIf MO/None)
		
	Raises:
		None
		
	Example:
		
	"""
	try:
		mo = vnic_fc_if_get(handle=handle, name=name, vnic_fc_dn=vnic_fc_dn, 
							   caller="vnic_fc_if_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def vnic_fc_if_modify(handle, name, vnic_fc_dn, **kwargs):
	"""
	modifies vnic fc
	
	Args:
		handle (UcsHandle)
		name (string): vnic fc name
		org_dn (string): location to place vnic fc
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		VnicFcIf: managed object
		
	Raises:
		UcsOperationError: if VnicFcIf is not present
		
	Example:
		
	"""
	
	mo = vnic_fc_if_get(handle=handle, name=name, vnic_fc_dn=vnic_fc_dn,
						   caller="vnic_fc_if_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def vnic_fc_if_delete(handle, name, vnic_fc_dn):
	"""
	deletes vnic ether
	
	Args:
		handle (UcsHandle)
		name (String): vnic fc name
		vnic_fc_dn (string): location to place vnic fc
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if VnicFcIf is not present
		
	Example:
		
	"""
	
	mo = vnic_ether_if_get(handle=handle, name=name, 
						   vnic_fc_dn=vnic_fc_dn, 
						   caller="vnic_fc_if_delete")
	handle.remove_mo(mo)
	handle.commit()
	
