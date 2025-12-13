
class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None, domain=None) -> None:
        raw_name = name if name is not None else self.anonymous_user().name
        
        if not raw_name.isalpha():
            if raw_name != "Anonymous": 
                raise ValueError("Ім'я може містити лише літери!")

        self.name = raw_name.capitalize() 

        self.domain = domain if domain is not None else MyName.DEFAULT_DOMAIN

        MyName.total_names += 1
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    
    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method
        """
        return f"You say: {message}"
    @property
    def name_length(self) -> int:
      """Повертає кількість символів в імені."""
      return len(self.name)

print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", None, "Oleh")
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")
marta = all_names.get("Marta") # Отримуємо об'єкт
if marta:
    print(f"Змінене привітання: {marta.say_hello('Вітаю вас від імені Марти!')}")
print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
print(f"Довжина імені Marta: {all_names['Marta'].name_length}")