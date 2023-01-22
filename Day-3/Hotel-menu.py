    
def menu_list():    
    punjabi_menu={1:"paneer makhani",2:"paneer kadai",3:"paneer toofani",4:"paneer butter masala"}
    gujarati_menu ={1:"sev tamatar",2:"bhindi",3:"oddo",4:"thepla"}
    southindian_menu={1:"dhosa",2:"idli",3:"medu vada",4:"uttapam"}
    marathi_menu={1:"sev usad",2:"kothmbirvadi",3:"pa bhaji",4:"vada pav"}

    menu={'Punjabi menu':punjabi_menu , 'Gujarati menu':gujarati_menu,'South Indian Menu':southindian_menu,'Marathi Menu':marathi_menu}

    return menu

def add_items_from_menu():

    print("Welcome to resturant , here's the menu . \n enjoy your meal")
    your_order={}

    while True:
        menu=menu_list()

        for key in menu.keys() :
            print(key)

        name=input("please select menu: ")
        for k,v in menu.items():
            if k==name :
                print(k , ":")
                for key , value in v.items():
                        print(key ," ", value )
                

        number = int(input("enter dish number :"))
        


        for k,v in menu.items():
            if k==name   :
                for key , value in v.items():
                    if key==number:
                        your_order[key]=value
                        print(key ," ", value )
        
        a = int(input("Do you want to add more dishes? (0=no/1=yes)"))
        if a==0:
            print("Your order: ")
            for v in your_order.values():
                 print( v)
            break;
        

if __name__ == "__main__":
    add_items_from_menu()
        
        
