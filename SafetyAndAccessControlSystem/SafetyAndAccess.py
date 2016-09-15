class SafetyAndAccess:
    
    def androidApplication(string, bool):
    #post to androidApplication
        print('Hello','World')
        
    def keyfob(self):
        #If keyfob/card present, do x
        print('Keyfob ')
        
    def doors(self, bool):
        #Lock/unlock doors
        if (bool == true):
            print('Doors have been locked')
        else:
            print('Doors have been unlocked')
        
    def airbags(self, bool):
        #Trigger airbags
        print('Airbags')
        
    def test(self):
        print('Hello','World')
    	
a = SafetyAndAccess()

a.test()
a.keyfob()
        