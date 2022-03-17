class m_override_base:

    def display(self):
        print("this is a method of BASE CLASS")


class m_override_derived(m_override_base):

    def display(self):
        print("this is a method of DERIVED CLASS")
        super().display()            # to access overridden method


ride_obj = m_override_derived()          # object of derived class
ride_obj.display()

"""a method having same name and arguments is used in both derived class as well as in base or super class 
The method used in derived class is said to override the method described in base class.
 Whenever the overridden method is called, it always invokes the method defined in derived class. 
 The method used in base class gets hidden. """
