

class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_link = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    lstitem_Administrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitem_Guests_xpath = "//li[contains(text(),'Guests')]"
    lstitem_Vendros_xpath = "//li[contains(text(),'Vendors')]"
    lstitem_ForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


