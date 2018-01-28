import urllib2,json
from texttable import Texttable

class Coin(object):
    def __init__(self,nama,volume,harga_beli,rate_sekarang):
        self.nama           = nama
        self.volume         = volume
        self.harga_beli     = harga_beli
        self.rate_sekarang  = rate_sekarang
        self.laba           = 0
        self.rugi           = 0
        self.cek_rugi_laba()
    def __str__(self):
        hasil = ""
        hasil += "[+] Coin         : {0}\n".format(self.nama)
        hasil += "[-] Volume       : {0}\n".format(self.volume)
        hasil += "[-] Harga Beli   : Rp.{:,.0f}\n".format(self.harga_beli)
        hasil += "[-] Rate Jual    : Rp.{:,.0f}\n".format(self.rate_sekarang)
        hasil += "[-] Harga Jual   : Rp.{:,.0f}\n".format(self.harga_jual())
        hasil += "[-] Laba         : Rp.{:,.0f}\n".format(self.laba)
        hasil += "[-] Rugi         : Rp.{:,.0f}\n".format(self.rugi)
        return hasil
    def harga_jual(self):
        return self.rate_sekarang * self.volume
    def cek_rugi_laba(self):
        nilai_sekarang = self.harga_jual()
        if(nilai_sekarang > self.harga_beli):
            ## UNTUNG
            self.laba = nilai_sekarang - self.harga_beli
            self.rugi = 0
        else:
            ## RUGI
            self.laba = 0
            self.rugi = self.harga_beli - nilai_sekarang
    def ambil_list(self):
        n_harga_beli    = "Rp.{:,.0f}".format(self.harga_beli)
        n_rate_sekarang = "Rp.{:,.0f}".format(self.rate_sekarang)
        n_laba          = "Rp.{:,.0f}".format(self.laba)
        n_rugi          = "Rp.{:,.0f}".format(self.rugi)
        return [self.nama,self.volume,n_harga_beli,n_rate_sekarang,n_laba,n_rugi]

class API_Vip():
    def __init__(self):
        pass
    def getBTC(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/btc_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getBCH(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/bch_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getBTG(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/btg_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getETH(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/eth_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getETC(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/etc_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getLTC(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/ltc_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getNXT(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/nxt_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getWAVES(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/waves_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getXLM(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/str_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getXRP(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/xrp_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)
    def getXZC(self):
        link    = urllib2.urlopen("https://vip.bitcoin.co.id/api/xzc_idr/ticker").read()
        nilai   = json.loads(link)['ticker']['last']
        return float(nilai)



## ASSET COIN
modal_utama = 50000000
total_laba  = 0
total_rugi  = 0
hasil_tmp   = "\n"
harga_utama = API_Vip()
table_utama = Texttable()
table_kolom = ['Coin','Volume','Harga Beli','Rate Sekarang','Laba','Rugi']
table_isi   = []
table_isi.append(table_kolom)

## BTC
harga_btc   = harga_utama.getBTC()
coin_btc    = Coin("BTC",0.08346844,15178212,harga_btc)
total_laba  += coin_btc.laba
total_rugi  += coin_btc.rugi
table_isi.append(coin_btc.ambil_list())

## ETH
harga_eth   = harga_utama.getETH()
coin_eth    = Coin("ETH",0.30181319,1984149,harga_eth)
total_laba  += coin_eth.laba
total_rugi  += coin_eth.rugi
table_isi.append(coin_eth.ambil_list())

## NXT
harga_nxt   = harga_utama.getNXT()
coin_nxt    = Coin("NXT",20,356020,harga_nxt)
total_laba  += coin_nxt.laba
total_rugi  += coin_nxt.rugi
table_isi.append(coin_nxt.ambil_list())

## XLM
harga_xlm   = harga_utama.getXLM()
coin_xlm    = Coin("XLM",30,116700,harga_xlm)
total_laba  += coin_xlm.laba
total_rugi  += coin_xlm.rugi
table_isi.append(coin_xlm.ambil_list())

## XRP
harga_xrp   = harga_utama.getXRP()
coin_xrp    = Coin("XRP",10,116700,harga_xrp)
total_laba  += coin_xrp.laba
total_rugi  += coin_xrp.rugi
table_isi.append(coin_xrp.ambil_list())


## XZC
harga_xzc   = harga_utama.getXZC()
coin_xzc    = Coin("XZC",8.76568034,11921196,harga_xzc)
total_laba  += coin_xzc.laba
total_rugi  += coin_xzc.rugi
table_isi.append(coin_xzc.ambil_list())


total_rugi += 1848446 ## RUGI TAK TERLIHAT
laba_akhir  = total_laba - total_rugi
total_asset = modal_utama + laba_akhir
hasil_tmp += "[+] Modal         : Rp.{:,.0f}\n".format(modal_utama)
hasil_tmp += "[+] Total Laba    : Rp.{:,.0f}\n".format(total_laba)
hasil_tmp += "[+] Total Rugi    : Rp.{:,.0f}\n".format(total_rugi)
hasil_tmp += "[+] Laba Akhir    : Rp.{:,.0f}\n".format(laba_akhir)
hasil_tmp += "[+] Total Asset   : Rp.{:,.0f}\n\n".format(total_asset)


## BTC #2
coin_btc2    = Coin("BTC #2",0.24878329,0,harga_btc)
total_laba  += coin_btc2.laba
total_rugi  += coin_btc2.rugi
table_isi.append(coin_btc2.ambil_list())

table_utama.add_rows(table_isi)
table_utama.set_cols_width([8,8,13,15,13,13])
print table_utama.draw()


laba_akhir  = total_laba - total_rugi
total_asset = modal_utama + laba_akhir
hasil_tmp += "[+] Laba Akhir    : Rp.{:,.0f}\n".format(laba_akhir)
hasil_tmp += "[+] Total Asset   : Rp.{:,.0f}\n".format(total_asset)

print hasil_tmp
