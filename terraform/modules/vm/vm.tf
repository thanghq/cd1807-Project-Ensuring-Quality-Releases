resource "azurerm_network_interface" "network_interface" {
  name                = "${var.application_type}-${var.resource_type}-nw-interface"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

resource "azurerm_linux_virtual_machine" "myVM" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group
  size                = "Standard_DS2_v2"
  admin_username      = "clark"
  network_interface_ids = [
    azurerm_network_interface.network_interface.id,
  ]
  admin_ssh_key {
    username   = "clark"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCaeR9JZ9J1Xwf+RbXEATnwFcUCCtS+adueKLQ8gZ2AXl4NW5Q3Z8QwtgaK76v1++yZ69RoQ6oLhP402aBOyoxwhJChmESTEBSb+YdbtGeVixbtslDi0K4x5BpoEKvpDq/zRHaRwImrKi/pClooC8aljrMfebOYC5IGBFrVSdPV6/mhcMX3Cz3njWIoiLdSkCuTDYkFHkzMDUNsyFzxwJSNuM50mUGRK1Q/tHRgXP/+yaAmbZ8Og3UFYdDKW6dQxoEa5ARkgUxCaqKVTDgufNTJPhUvcHBAIPnfsF33dmsDZ1aN1Eq6yU0kkBk/PHtudRuSpJ0VuU9YOVGcbQ/ZYg40a1Nsr+ZKyJ6YOvh7l14fkMN6i1gTGrVM0w+SGEDQ78KNLSFlGF+ztVaMxG5931RoJdmBJiuOEmqNYfcj+x8py7Dy4VyCnobp6QJgOjGXFKuqomIKJcBTb1I5Bx5LPUJM+wCDniAAzewzTfCY0mrWCTfDjH7c12QUll2rfdf/nvM= clark-hoang@Clarks-MacBook-Pro.local"
  }
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
