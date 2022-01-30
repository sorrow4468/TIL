import timeit
start = timeit.default_timer()

text = 'aawneifonoeiwmcl,xjfklsajdfklajewklfhaefnk1r7e8yiueniuencieh02cf12fh0v3ymn,cgjklo10f321hcqvyjkn9og4ml0f21hc3v9yjknqom0h1vcf2y93njkmof210hc3v9jkoymn0f21hcvko9jnym021hfok9cqv3jln,210hf9ocv3jklmny,qgf21h0kmn,jlocqv39cf30hkv9mn,ojlgfvc0hkx12mn,jol9210cf3hk9qvomn,jl10fh9cv3okjmn,g10cf3hv9knom0f9h3koncvm,02f1h9kcv3omn,j2f103vhc9knmjog0f2h19kncv3jmoyg0f21h9cv3njkgmoy0fh921ojkymncgv3,rlf21h0c3v9nyjkmgoh0n9f2yjkmcv13g4h0f21c3vn9kmjyg0hf219ncvjkm3og0f21hc3v9mnjky,o0f21hcvn9km3jy0h1vcf2nk9mj3021hnkf9m,cv3jhf210ncv3mjk9h0f219nycv3jkg0h9f21nycv3jk0h9f21nycv3kjg0fh219mnjkcv3,yogf20h1v3n9cg4kmf0h2913vcgf3210cvh9g4n20f31h9cvnkgf02h9c13vngtkr40fh921nkcvm30hn9kfmcv3h0nf1mk,j9cv3gf,mn12v0chkljox30cf21hkv3mn,9of0cmn,hkvjlo390hk9omnj,2f13vc0h9nk1mojfc3v0h9n12cfkmv3021h9cfnvyh0nf29kmcv13jh29fn1kmcv30f2h91ncvkm30h92nkf1mcv3o0h9f21nkmocv,30h9nk2fmcv130h9fknc12v30h9nk12fmcv320hc9f1nvk30f2h9c1vnkm30h9fnkc1vh9nkmjof12cv30h9fnkmcv12o,30h9f21nkcvmx30hf9n12ckv30h9nfkmc12v30hk9n,mfjloc1v0fh912vcnk3mh9f12vcn30h9nkcf12v30hf2n91mcv0hnf9c12v3h0n9mkj2cfv130h9nfc12v30h9fnkcv12m3gf219hcvn3kg0f21h9cvn3f219hcvk3nf021h9cnv39hf21cv30h9nf2c1vg3h09n1f2ycvg30h9fnc12vy8g3df09h2c1vg30h98y7nfcv213gh0987yfv2c13h0987yf2cv13ghy0987ncfv123h09872fyv134chyf7098cv2g09h87fv2cg13hy67098cv12gh09f21ycv3g4h09y87f12v3cg0h9821vc309h8f12cv309hfcv09hn12vcx309hn1f2cv30h9nf12cv30hn1cf2'
pattern = 'cx309hn1f2cv30h9'
result = 0
for i in range(len(pattern)-1, len(text)):
    if text[i] == pattern[-1]:
        j = 2
        while True:
            if pattern[-j] == text[i-j+1]:
                if pattern[-j] == pattern[0]:
                    result = 1
                    break
                else:
                    j += 1
            else:
                break
print(result)

end = timeit.default_timer()
print(f'{end-start:.5f}')