class Pelayan:
    def __init__(self, nama, shift, notelp):
        self.nama = nama 
        self.shift = shift
        self.notelp = notelp

    def info(self):
        nama = input("Masukkan Nama Pelayan : ")
        notelp = input("Nomor Telepon Pelayan : ")
        print("Nama Pelayan adalah ",nama)
        print("No Telepon pelayan adalah ",notelp)
        print ("Pelayan yang melayani anda adalah %s, shift %s, dengan nomor telepon %s." %(self.nama, self.shift, self.notelp))
        pembeli = input("Masukkan nama Pembeli: ")
        notelp1 = input("Nomor Telepon Pembeli :")
        print ("Nama Pembeli :", pembeli) 
        print ("Nomor telepon pembeli adalah ", notelp1)
