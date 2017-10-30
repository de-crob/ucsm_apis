"""
This module intends on creating higher level api calls for establishing an
 Ls Server (the base object for a server profile template)
"""
from ucsmsdk.ucsexception import UcsOperationError


def ls_server_create(handle, name, org_dn="org-root", agent_policy_name=None,
					 bios_profile_name=None, boot_policy_name=None, descr=None,
					 dynamic_con_policy_name=None, ext_ip_pool_name=None, 
					 ext_ip_state="none", host_fw_policy_name=None, 
					 ident_pool_name=None, kvm_mgmt_policy_name=None,
					 local_disk_policy_name=None, maint_policy_name=None,
					 mgmt_access_policy_name=None, mgmt_fw_policy_name=None,
					 policy_owner="local", power_policy_name="default", 
					 power_sync_policy_name=None, resolve_remote=None,
					 scrub_policy_name=None, sol_policy_name=None,
					 src_templ_name=None, stats_policy_name="default", 
					 type="initial-template", usr_lbl=None , uuid="derived", 
					 vcon_profile_name=None, vmedia_policy_name=None, **kwargs):
			   
	"""
	creates the service template

	Args:
		handle (UcsHandle)
		name (string): ls server name
		org_dn (string): location to place ls server
		agent_policy_name (string):
		bios_profile_name (string): 
		boot_policy_name (string):
		descr (string):
		dynamic_con_policy_name(string):
		ext_ip_pool_name (string):
		ext_ip_state (string): valid values are "none" or "pooled", or "static"
		host_fw_policy_name (string):
		ident_pool_name (string):
		kvm_mgmt_policy_name (string):
		local_disk_policy_name (string):
		maint_policy_name (string):
		mgmt_access_policy_name (string):
		mgmt_fw_policy_name (string):
		policy_owner (string): "local" or "pending-policy" or  "policy"
		power_policy_name (string):
		power_sync_policy_name (string):
		resolve_remote (string): 'yes' or 'no'
		scrub_policy_name (string):
		sol_policy_name (string):
		src_templ_name (string):
		stats_policy_name (string):
		type (string): "initial-template" or "instance" or "updating-template"
		usr_lbl (string):
		uuid (string):
		vcon_profile_name (string):
		vmedia_policy_name (string):
		**kwargs: Any additional key-value pair of managed object(MO)'s
                  property and value, which are not part of regular args.
                  This should be used for future version compatibility.
				  
	Returns:
		LsServer: managed object
		
	Raises:
		UcsOperationError: if OrgOrg is not present
	
	Example:
		
	"""
	
	from ucsmsdk.mometa.ls.LsServer import LsServer
	
	obj = handle.query_dn(org_dn)
	
	if not obj:
		raise UcsOperationError("ls_server_create", "Org '%s' does not exist" \
								% org_dn)
								
	mo = LsServer(parent_mo_or_dn=obj, name=name, 
				  agent_policy_name=agent_policy_name,
				  bios_profile_name=bios_profile_name, 
				  boot_policy_name=boot_policy_name, descr=descr, 
				  dynamic_con_policy_name=dynamic_con_policy_name,
				  ext_ip_pool_name=ext_ip_pool_name,
				  ext_ip_state=ext_ip_state, 
				  host_fw_policy_name=host_fw_policy_name,
				  ident_pool_name=ident_pool_name,
				  local_disk_policy_name=local_disk_policy_name,
				  maint_policy_name=maint_policy_name, 
				  mgmt_access_policy=mgmt_access_policy, 
				  mgmt_fw_policy_name=mgmt_fw_policy_name,
				  policy_owner=policy_owner, 
				  power_policy_name=power_policy_name, 
				  resolve_remote=resolve_remote, 
				  scrub_policy_name=scrub_policy_name, 
				  sol_policy_name=sol_policy_name, 
				  src_templ_name=src_templ_name,
				  stats_policy_name=stats_policy_name, type=type,
				  usr_lbl=usr_lbl, uuid=uuid, 
				  vcon_profile_name=vcon_profile_name, 
				  vmedia_policy_name=vmedia_policy_name)
				  
	mo.set_prop_multiple(**kwargs)
	handle.add_mo(mo, modify_present = True)
	handle.commit()
	return mo
	
def ls_server_get(handle, name, org_dn="org-root", caller="ls_server_get"):
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
		UcsOperationError: if LsServer is not present
		
	Example:
		
	"""

	dn = org_dn + "/ls-" + name
	mo = handle.query_dn(dn)
	if mo is None:
		raise UcsOperationError(caller, "LsServer '%s' does not exist" % dn)
	return mo
	
def ls_server_exists(handle, name, org_dn="org-root", **kwargs):
	"""
	checks if ls server exists
	
	Args:
		handle(UcsHandle)
		name (string): ls server name
		org_dn (string): location to place ls server
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		(True/False, LsServer mo/None)
		
	Raises:
		None
		
	Example:
		
	"""
	
	try:
		mo = ls_server_get(handle=handle, name=name, org_dn=org_dn, 
						   caller="ls_server_exists")
	except UcsOperationError:
		return (False, None)
	
	mo_exists = mo.check_prop_match(**kwargs)
	return (mo_exists, mo if mo_exists else None)
	
def ls_server_modify(handle, name, org_dn="org-root", **kwargs):
	"""
	modifies ls server
	
	Args:
		handle (UcsHandle)
		name (string): ls server name
		org_dn (string): location to place ls server
		**kwargs: key-value pair of managed object(MO) property and value, Use
                  'print(ucscoreutils.get_meta_info(<classid>).config_props)'
                  to get all configurable properties of class
				  
	Returns:
		LsServer: managed object
		
	Raises:
		UcsOperationError: if LsServer is not present
		
	Example:
		
	"""
	
	mo = ls_server_get(handle=handle, name=name, org_dn=org_dn, 
					   caller="ls_server_modify")
					   
	mo.set_prop_multiple(**kwargs)
	handle.set_mo(mo)
	handle.commit()
	return mo
	
def ls_server_delete(handle, name, org_dn="org-root"):
	"""
	deletes ls server
	
	Args:
		handle (UcsHandle)
		name (String): ls server name
		org_dn (string): location to place ls server
		
	Returns:
		None
	
	Raises:
		UcsOperationError: if LsServer is not present
		
	Example:
		
	"""
	
	mo = ls_server_get(handle=handle, name=name, org_dn=org_dn, 
					   caller="ls_server_delete")
	handle.remove_mo(mo)
	handle.commit()