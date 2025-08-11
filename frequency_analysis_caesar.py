#Assignment 2 : Frequency Analysis Attack
#Implement a Cryptanalysis attack on ciphertext generated using Caesar cipher and try to find key for the same.

#1.Use the  string  of english letters "ETAOINSHRDLCUMWFGYPBVKJXQZ" in the decreasing frequency order, according to the english language.
#2. Use given Ciphertext and find the key for the same.


import string

def caesar_decrypt(ciphertext, key):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base - key) % 26 + base
            decrypted.append(chr(shifted))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def frequency_analysis(ciphertext):
    # English letter frequency order
    english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # Count frequency of letters in ciphertext (case insensitive)
    freq = {}
    for char in ciphertext.upper():
        if char in string.ascii_uppercase:
            freq[char] = freq.get(char, 0) + 1

    # Sort letters in ciphertext by frequency descending
    sorted_cipher_letters = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    if not sorted_cipher_letters:
        return None, None

    # Most frequent letter in ciphertext
    most_freq_cipher_letter = sorted_cipher_letters[0][0]

    # Assume most frequent letter in ciphertext corresponds to 'E' (most frequent in English)
    assumed_plain_letter = 'E'

    # Calculate key as the shift between most frequent ciphertext letter and 'E'
    key = (ord(most_freq_cipher_letter) - ord(assumed_plain_letter)) % 26

    # Decrypt ciphertext with estimated key
    decrypted_text = caesar_decrypt(ciphertext, key)

    return key, decrypted_text

if __name__ == "__main__":
    ciphertext = """LPHWXCVIDC Rdbxcv dji xc hjeedgi du Pccp Wpopgt Xcsxpc Pbtgxrpch wpkt peetpats id iwt Xcsxpc vdktgcbtci id ipzt htgxdjh hiteh id rjgq iwt btcprt du rdggjeixdc xc iwt rdjcign

Lt CGXh lpci id gtbdkt rdggjeixdc dji du Xcsxp. Lt hjeedgi Pccp Wpopgt'h tuudgih id tgpsxrpit iwt rdggjeixdc ephh Adzepa Qxaa pcs strapgt qaprz bdctn ph cpixdcpa phhtih hpxs Scnpcdqp Ztcsgt p ndvp itprwtg ugdb Etcchnakpcxp

Du paa iwt egdithih xc Xcsxp xc gtrtci ixbth, iwxh xh iwt bdhi atvxixbpit pcs pi iwt vgphh gddi-atkta iwpi rpc rwpcvt iwt upit du iwt rdjcign hpxs Gpcvpgpypc p hijstci ugdb iwt Jcxktghxin du Bpgnapcs

Pcdiwtg hijstci Jbpcv Pvpgplpa, hpxs iwtn pgt tbpxaxcv Hjegtbt Rdjgi tc bphh sxgtrian id ipzt hjd bdij prixdc pcs hpkt iwt cpixdc

Bdgt iwpc Xcsxpch uxvwixcv pvpxchi rdggjeixdc xi httbh vdktgcbtci xh uxvwixcv pvpxchi etdeat lwd pgt uxvwixcv pvpxchi rdggjeixdc. Iwxh xh vdxcv id qt dct du iwt lpitghwts bdbtcih du Xcsxpc wxhidgn hpxs Kxqwphw Ywp p EwS hijstci pi iwt Jcxktghxin du Bpgnapcs. 

Xcsxpc-Pbtgxrpch ugdb xc pcs pgdjcs Lphwxcvidc udg iwt iwxgs spn wtas p stbdchigpixdc xc ugdci du iwt Xcsxpc tbqphhn wtgt. Hxbxapg tktcih xc hjeedgi du Wpopgt pgt qtxcv gtedgits ugdb kpgxdjh epgih du iwt rdjcign ph ltaa. 

P apgvt cjbqtg du Xcsxpc-Pbtgxrpch wtas p hxbxapg egdithi stbdchigpixdc djihxst iwt Xcsxpc Rdchjapit xc Wdjhidc. 

Lt CGX xc Wdjhidc utta rdcctrits id iwt bdktbtci xc Xcsxp pcs pgt tmegthhxcv hjeedgi xc htktgpa udgbh axzt Uprtqddz Ilxiitg Vddvat ltqhxith xc pssxixdc id iwtxg egthtcrt xc adrpa vpiwtgxcvh pgdjcs pepgibtci rajq wdjhth, ejqaxr epgzh pcs diwtg rdbbjcxin eaprth hpxs Gpvwpkp G Hdaxejgpb. 

Hwdrzts pcs hpsstcts qn iwt pggthi du Wpopgt pcs wxh hjeedgitgh Cdc-Gthxstci Xcsxpch udg Htrjapg pcs Wpgbdcxdjh Xcsxp (CGX-HPWX) hpxs Xcsxpc-Pbtgxrpch hjeedgi iwt stbpcs du Itpb Pccp id qgxcv tktgn dct jcstg iwt Ypc Adz Epa Qxaa. 

Lt stbpcs iwt vdktgcbtci du Xcsxp ztte xih egdbxht pcs egdbjavpit pc tuutrixkt Pcix-Rdggjeixdc Qxaa CGX-HPWX hpxs. 

Xc p hipitbtci, Piapcip-qphts JH Wxcsj Paaxpcrt higdcvan rdcstbcts iwt btphjgth ipztc qn iwt Xcsxpc vdktgcbtci pvpxchi iwt etprtuja pcs stbdrgpixr pcix-rdggjeixdc bdktbtci ats qn Wpopgt. 

Iwt gxvwi id hetpz ugttan pcs iwt gxvwi id egdithi etprtujaan wpkt qttc tpgcts qn iwt etdeat du Xcsxp puitg p egdadcvts higjvvat lwxrw xckdakts iwt hprgxuxrth du bxaaxdch du xih etdeat. 

Wxcsjh pgdjcs iwt ldgas rpccdi gtbpxc hxatci hetripidgh lwtc iwt vdktgcbtci hcpirwth plpn iwt ugjxih du Xcsxp'h ugttsdb bdktbtci pcs piitbeih id rgtpit p edaxixrpa tckxgdcbtci lwxrw wph paa iwt wpaabpgzh du p edaxrt hipit xi hpxs."""

    key, decrypted_text = frequency_analysis(ciphertext)
    if key is not None:
        print(f"Estimated key: {key}")
        print("\nDecrypted text:\n")
        print(decrypted_text)
    else:
        print("Could not estimate key from ciphertext frequency analysis.")
