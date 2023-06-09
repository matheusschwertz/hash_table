class Veiculo:
    def __init__(self, placa, ano, marca_modelo, cor):
        self.size = 29
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.placa = placa
        self.ano = ano
        self.marca_modelo = marca_modelo
        self.cor = cor
    def __str__(self):
        return '{} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)
    def __repr__(self):
        return '{} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key 
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __str__(self):
        return '{} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)
    
    def __repr__(self):
        return '{} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)
    

H=Veiculo()

print(H.slots)
print(H.data)
