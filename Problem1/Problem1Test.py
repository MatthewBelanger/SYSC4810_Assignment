import Role
import User

def main():
    #Create roles
    regularClientRole = Role.Role("Regular Client")
    premiumClientRole = Role.Role("Premium Client")
    financialAdvisorRole = Role.Role("Financial Advisor")
    financialPlannerRole = Role.Role("Financial Planner")
    investmentAnalystRole = Role.Role("Investment Analyst")
    complianceOfficerRole = Role.Role("Compliance Officer")
    technicalSupportRole = Role.Role("Technical Support")
    tellerRole = Role.Role("Teller")

    #Create users
    mischa = User.User("mischa", "Mischa Lowery", regularClientRole)
    veronica = User.User("veronica", "Veronica Perez", regularClientRole)
    winston = User.User("winston", "Winston Callahan", tellerRole)
    kelan = User.User("kelan", "Kelan Gough", tellerRole)
    nelson = User.User("nelson", "Nelson Wilkins", financialAdvisorRole)
    kelsie = User.User("kelsie", "Kelsie Chang", financialAdvisorRole)
    howard = User.User("howard", "Howard Linkler", complianceOfficerRole)
    stefania = User.User("stefania", "Stefania Smart", complianceOfficerRole)
    willow = User.User("willow", "Willow Garza", premiumClientRole)
    nala = User.User("nala", "Nala Preston", premiumClientRole)
    stacy = User.User("stacy", "Stacy Kent", investmentAnalystRole)
    keikilana = User.User("keikilana", "Keikilana Kapahu", investmentAnalystRole)
    kodi = User.User("kodi", "Kodi Matthews", financialPlannerRole)
    malikah = User.User("malikah", "Malikah Wu", financialPlannerRole)
    caroline = User.User("caroline", "Caroline Lopez", technicalSupportRole)
    pawel = User.User("pawel", "Pawel Barclay", technicalSupportRole)


    #Create list of all users for testing
    userList = [mischa, veronica, winston, kelan, nelson, kelsie, howard,
                stefania, willow, nala, stacy, keikilana, kodi, malikah, caroline, pawel]
    
    #Output all users along with their permissions
    for user in userList:
        print(user.getName() + " has the role: " + user.getRole() + " they have access to the following:")
        perms = user.getPermissions()
        for perm in perms:
            print(perm + "=" + perms[perm])  
        print("\n")  
    
main()