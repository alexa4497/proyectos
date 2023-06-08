import datetime
import io


ahora=datetime.datetime.now()

class Criptomonedas(object):
        def __init__(self, nombre,  cantidad, cotizacion, transacción):
                self.nombre = nombre
                self.cantidad = cantidad
                self.cotizacion = cotizacion
                self.transacción = transacción
                
        def Nombre(self, nombre):
                self.nombre=nombre
 
        def cantidad(self, cantidad,):  
                self.cantidad=cantidad

        def cotizacion(self, cotizacion):
                self.cotizacion=cotizacion

        def transacción(self, transacción):
                self.transacción=transacción
        
        def mostar_cotizacion(self):
                return self.nombre

        def mostrar_Nombre(self):
                return self.nombre
 
        def mostrar_cantidad(self):  
                return self.cantidad

        def mostar_transaccion(self):
                return self.transacción
        
        
bitcoin=Criptomonedas("BTC",0,0,0)
ethereum=Criptomonedas("ETH",0,0,0)
Dogecoin=Criptomonedas("BCC",0,0,0)
Litecoin=Criptomonedas("LTC",0,0,0)


monedas={"BTC":"bitcoin","ETH":"Ethereum","BCC":"Dogecoin","LTC":"Litecoin"}  
cod_usuario=22309
criptos = ["BTC","BCC","LTC","ETH","bitcoin","ethereum","Dogecoin","Litecoin"]


print("                                                                      ")
print("----------------------------------------------------------------------")
print("                  ¡Bienvenido a tu billetera digital!                 ")
print("----------------------------------------------------------------------")
print("                                                                      ")

n=input("¿cual es tu nombre?: ")


print("")
print("a continuacion el menu de opciones",n, ",tu codigo de usuario es ",cod_usuario)

while True:
        print("--------------------▼--------------------")
        print("1. recibir cantidad")
        print("2. transferir monto")
        print("3. mostrar balance de una moneda")
        print("4. mostar balance general")
        print("5. mostrar historico de transacciones")
        print("6. salir del programa")
        print("--------------------▲--------------------")
        print("")       
        opciones=int(input("ingrese una opcion del menu anterior: "))
        if opciones == 1:
                archivo=open("transacciones.txt","a+")
                while True:  
                        codigo=int(input("ingrse su codigo de usuario: "))
                        if codigo == cod_usuario:
                                print("codigo valido")
                                break
                        else:
                                print("codigo invalido")
                can1=int(input("indique la cantidad que desea recibir en dolares: "))

                while True:
                        moneda=input("ingrese el tipo de moneda que desea recibir(BTC,ETH,BCC,LTC): ")
                        if moneda in monedas:
                                print("moneda valida")
                                break
                        if not moneda in monedas:
                                print("moneda invalida")
                if moneda == "BTC":
                        bitcoin.cantidad=(can1+bitcoin.cantidad)
                        bitcoin.cotizacion=(can1+bitcoin.cotizacion)
                        archivo.write(ahora.strftime(" el dia %d/%m/%Y a las %H:%M:%S se recibio un monto de "+str(can1)+moneda+"  "+"\n"))
                        print("!transacion exitosa¡")
                        
                elif moneda== "BCC":
                        Dogecoin.cantidad=(can1+Dogecoin.cantidad)
                        Dogecoin.cotizacion=(can1+Dogecoin.cotizacion)
                        archivo.write(ahora.strftime(" el dia %d/%m/%Y a las %H:%M:%S se recibio un monto de "+str(can1)+moneda+"  "+"\n"))
                        print("!transacion exitosa¡")

                elif moneda == "LTC":
                        Litecoin.cantidad=(can1+Litecoin.cantidad)
                        Litecoin.cotizacion=(can1+Litecoin.cotizacion)
                        archivo.write(ahora.strftime(" el dia %d/%m/%Y a las %H:%M:%S se recibio un monto de" +str(can1)+moneda+"  "+"\n"))
                        print("!transacion exitosa¡")

                else:
                        moneda == "ETH"
                        ethereum.cantidad=(can1+ethereum.cantidad)
                        ethereum.cotizacion=(can1+ethereum.cotizacion)
                        archivo.write(ahora.strftime(" el dia %d/%m/%Y a las %H:%M:%S se recibio un monto de "+str(can1)+moneda+"  "+"\n"))
                        print("!transacion exitosa¡")
                archivo.close()
        if opciones == 2 :
                archivo=open("transacciones.txt","a+")
                while True:
                        codigo=int(input("ingrse su codigo de usuario: "))
                        if codigo == cod_usuario:
                                print("codigo valido")
                                break
                        else:
                                print("codigo invalido")
                while True:
                        moneda2=input("indique el tipo de moneda que desea tranferir(BTC,ETH,BCC,LTC): ")
                        if moneda2 in monedas:
                                print("moneda valida")
                                break
                        if not moneda2 in monedas:
                                print("moneda invalida")
                transferir=int(input("ingrese la cantidad a transferir: "))
                emi=int(input("código del destinatario a enviar:"))
                if moneda2 == "BTC":
                        if transferir < bitcoin.cantidad:
                                bitcoin.cantidad=(bitcoin.cantidad-transferir)
                                bitcoin.transacción=(bitcoin.transacción+transferir)
                                archivo.write(ahora.strftime("el dia %d/%m/%Y a las %H:%M:%S se realizo una transacción de "+str(transferir)+moneda2+"\n"))
                                print("!transacion exitosa¡")
                        else:
                                transferir > bitcoin.cantidad
                                print("cantidad insuficiente")
                                
                elif moneda2 == "LTC":
                        if transferir < Litecoin.cantidad:
                                Litecoin.cantidad=(Litecoin.cantidad-transferir)
                                Litecoin.transacción=(Litecoin.transacción+transferir)
                                archivo.write(ahora.strftime("el dia %d/%m/%Y a las %H:%M:%S se realizo una transacción de"+str(transferir)+moneda2+"\n"))
                                archivo.close()
                                print("!transacion exitosa¡")
                        else:
                                transferir > Litecoin.cantidad
                                print("cantidad insuficiente")

                elif moneda2 ==  "ETH":                
                        if transferir < ethereum.cantidad:
                                ethereum.cantidad=(ethereum.cantidad-transferir)
                                ethereum.transacción=(ethereum.transacción+transferir)
                                archivo.write(ahora.strftime("el dia %d/%m/%Y a las %H:%M:%S se realizo una transacción de "+str(transferir)+moneda2+"\n"))
                                print("!transacion exitosa¡")

                        else:
                                transferir > ethereum.cantidad
                                print("cantidad insuficiente")
                                
                else:
                        moneda2 == "BCC"
                        if transferir < Dogecoin.cantidad:
                                Dogecoin.cantidad=(Dogecoin.cantidad-transferir)
                                Dogecoin.transacción=(Dogecoin.transacción+transferir)
                                archivo.write(ahora.strftime("el dia %d/%m/%Y a las %H:%M:%S se realizo una transacción de "+str(transferir)+moneda2+"\n"))
                                print("!transacion exitosa¡")


                        else:
                                transferir > Dogecoin.cantidad
                                print("cantidad insuficiente")
                archivo.close()
                
        if opciones == 3:
                while True:
                        balance=input("indique la moneda a en la que desea ver el balance: ")
                        if balance in monedas:
                                print("moneda valida")
                                break
                        if not balance in monedas:
                                print("moneda invalida")

                if balance == "BTC":
                        print("balance total de BTC = ",bitcoin.cantidad)

                elif balance == "LTC":
                        print("balance total de LTC = ",Litecoin.cantidad)

                elif balance == "BCC":
                        print("balance total de BCC = ",Dogecoin.cantidad)

                else:
                        balance == "ETH"
                        print("balance total de ETH = ",ethereum.cantidad)

        if opciones == 4:
                saldototal=bitcoin.cantidad+ethereum.cantidad+Dogecoin.cantidad+Litecoin.cantidad
                print("el balancce total de su billetera dijital es: ")
                print("saldo total = ",saldototal)
                print("BTC = ",bitcoin.cantidad)
                print("LTC = ",Litecoin.cantidad)
                print("ETH = ",ethereum.cantidad)
                print("BCC = ",Dogecoin.cantidad)
        
        if opciones == 5:
                archivo=open("transacciones.txt","r")
                contenido=archivo.read()
                print(contenido)
                archivo.close()

        if opciones == 6:
                exit(1)