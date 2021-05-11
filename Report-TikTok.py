#KING M3GON
#========================================
#Have you installed desks , Iets's check that out
#try
try:
    #import requests
    import requests
#except
except:
    #pip install requests
    print('[-] pip install requests')
#try
try:
    from colorama import Fore
    import colorama
    colorama.init(autoreset=colorama)
#except
except:
    #pip install requests
    print('[-] pip install colorama')
import re
import time
import os
#def banner():
def banner():
    Bb = Fore.LIGHTYELLOW_EX
    print(Bb + """
        __  __ ____   _____  ____  _   _ 
        |  \/  |___ \ / ____|/ __ \| \ | |
        | \  / | __) | |  __| |  | |  \| |
        | |\/| ||__ <| | |_ | |  | | . ` |
        | |  | |___) | |__| | |__| | |\  |
        |_|  |_|____/ \_____|\____/|_| \_|
    """, Fore.LIGHTGREEN_EX + "\n                  ( @_m3gon )",
          Fore.LIGHTBLUE_EX + "\n   (This tool is programmed by the programmer : @_m3gon)              \n",
          Fore.LIGHTYELLOW_EX + "                ( Report TikTok )\n\n" + Fore.RESET)
banner()
#sessionid
sessionid = input('[?] Enter Sessionid : ')
#def check_sessionid_true_or_error():
def check_sessionid_true_or_error():
    global sessionid
    #url_check_sessionid
    url_check_sessionid = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6904193135771207173&os_version=14.2&app_id=1233&iid=6946987757887047426&app_name=musical_ly&vendor_id=3E86AE5D-1475-4A78-A34E-DCE1C9091FFE&locale=ar&ac=WIFI&sys_region=SA&ssmix=a&version_code=17.7.0&vid=3E86AE5D-1475-4A78-A34E-DCE1C9091FFE&channel=App%20Store&op_region=SA&os_api=18&idfa=D78BAC01-848D-4371-A604-7C3F3D678058&install_id=6946987757887047426&idfv=3E86AE5D-1475-4A78-A34E-DCE1C9091FFE&device_platform=iphone&device_type=iPhone10%2C6&openudid=59e0801cc11a5b89f399df1e1ad749afeed69600&account_region=&tz_name=Asia%2FRiyadh&tz_offset=10800&app_language=ar&carrier_region=SA&current_region=SA&aid=1233&mcc_mnc=42001&screen_width=1125&uoo=0&content_language=&language=ar&cdid=ECAD5F87-4334-4228-94D0-1D9958FC4EBD&build_number=177015&app_version=17.7.0&resolution=1125%2A2436'
    #headers_check_sessionid
    headers_check_sessionid = {
        'Host': 'api16-normal-c-alisg.tiktokv.com',
        'Connection': 'close',
        'Content-Length': '31',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-SS-Cookie': f'multi_sids=6778236784885122054%3A41059648ecde93eba0a905c184651adf%7C6946966238849844225%3A953d24738a88f45b4ca12f431525b848%7C6946988349706601473%3A41689832094ae90ae74053275dad09a5; odin_tt=c71c4d9ee4202c651a57ac5b0374a372d9d76f8fca63c3685caf68dac157bccde371c79258427c0ebfef25e27f154f3e2050bae55372e2584203c52780933ddf; sessionid=41689832094ae90ae74053275dad09a5; sessionid_ss=41689832094ae90ae74053275dad09a5; sid_guard=41689832094ae90ae74053275dad09a5%7C1617472026%7C5184000%7CWed%2C+02-Jun-2021+17%3A47%3A06+GMT; sid_tt=41689832094ae90ae74053275dad09a5; store-country-code=sa; store-idc=alisg; uid_tt=9719aa5f7b71b36a7208cec16e785653f095610219b8e792127acff7f77203bf; uid_tt_ss=9719aa5f7b71b36a7208cec16e785653f095610219b8e792127acff7f77203bf; install_id=6946987757887047426; ttreq=1$c6ea408e3f2a28056cb33132cca7c7d29e77992b; cmpl_token=AgQQAPO_F-RPsLBWeltddB04xbEGIBnKf4c0YPjPAA; d_ticket=ab7d42861b134f5a7cefb8addd65d9ceea3a4; passport_csrf_token={sessionid}; passport_csrf_token_default={sessionid}',
        'tt-request-time': '1617472075991',
        'User-Agent': 'TikTok 17.7.0 rv:177015 (iPhone; iOS 14.2; ar_SA@calendar=gregorian) Cronet',
        'x-tt-passport-csrf-token': sessionid,
        'Accept-Encoding': 'gzip, deflate',
        'X-Khronos': '1617472074',
        'X-Gorgon': '840280396000b30fdab8cc3fa84c05f5a04e008f327ac53688fc'
    }
    #cookies_check_sessionid
    cookies_check_sessionid = {'sessionid': sessionid}
    #data_check_sessionid
    data_check_sessionid = {'login_name': ''}
    #req_check_sessionid
    req_check_sessionid = requests.post(url_check_sessionid, data=data_check_sessionid, headers=headers_check_sessionid, cookies=cookies_check_sessionid).text
    if ('"description":"معلمات مفقودة"') in req_check_sessionid:
        print(Fore.LIGHTGREEN_EX + '[+] Logged In')
        #username_target
        username_target = input('[?] Enter Username Target : ')
        #def get_id_target():
        def get_id_target():
            #url_get_id
            url_get_id = f'https://www.tiktok.com/@{username_target}?'
            #headers_get_id
            headers_get_id = {
                'Host': 'www.tiktok.com',
                'Cookie': 'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; webapp_tiktok_lang=ar; tta_attr_id=0.1616499265.6942811476331593729; s_v_web_id=verify_kmxb0dd5_U5SMVNWR_g0Au_4r8J_9Qe3_NJxpQO88j1Pw; store-idc=alisg; store-country-code=sa; odin_tt=9e36bc7e668adaca285bdabfdc5522cae25ab7d5a6a56ef8880573ef4c692fdc1f7525f56ac9e3e77660cc380ad65f677e6b00464a9537d5bd8579e837063d3e19601cb7c2bfc2670cffac88be90fe15; ttwid=1%7Cgi8ynNW57o66_fiDbhBjBs9nnuaeZv-1OTK3G5gmasg%7C1620413005%7C394bbe09c3b44c4c9888d610307e0bac9d529e828f5039a5dc2e70b3727ca482; tt_csrf_token=biBAjWPswn1Ia8d_7rsdywQa; MONITOR_WEB_ID=6940688826462406145; R6kq3TV7=AJL0p1x5AQAAgZ7UVUQ6Z_KKbbeh5V5rk1UaC0j4uVifRF8UZNUVrUJz9fFZ|1|0|bde1f506e2e120b4c97406a027a957d96a261126; csrf_session_id=f542d4c150684c8f8b565e56b620bff7; ak_bmsc=22C2B083F339CBE14339EFA65156A32656335E77BE330000BFCA9A6082EF1008~pl9qoJSA+vGmaFbpQTQUctlmE8lshSuY6YHoGK6eAFcwNGgFZsreTcrHNbxxGmpbl2GeyKL5276g5I/XQbSNpcwrr3cLsZ08fYr1T8IsmfB4yVD4pNbOvvocKs0Kwp4oGdquXtKten+dumIsbOYePAhDb4MopA6mBiXQ7IMKkZ66Gs9jhPn/1L7izxuAnlkvBQ2t4Ll3JgjK10tgMrmeooyS384GIBMU/9anOAEvzrh5c=; bm_sz=922FB4C8CA0E7C5EE7AAE96ED45A8D14~YAAQd14zVmmwGkJ5AQAAifunXAu6DUsNarpL0o3/MO2WbnFS6FTTWKwxn2twV02yxkLnXZhK4KuYsQdEvSzvN5Waphqt67i1QrSkqjqjrI+ud2Ipf8kP0aYBPU3F6aZBaTASUC/LPWyw6VSsJBdp2axybcksh9iN4tbe8ckxe0fS9e0HXMtG4zg14NKmCMF2; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQd14zVmqwGkJ5AQAAifunXAXD2Rm1wrf/kCpyHcjNt90XMNyT40T79i2Xiiv/+D7cSh+qO0hCvwfZPOdJLl1TZ/+70kjAkZhxQANKmbR1eG3hCoYziKZOVlLnIM4FvKCjI/8I0Ttyo2MPgy0k0Xd7aFV0JK9JNU0NBZTw4uTAjkpipxbcRFPw0Dzd6fxASkgbhUwGK866PwyfbVVffdeIqZ3USzyrTk6DR8lrU0M6tgsoRbx1/UY+Ue5MFQODr9n56Z6y/6LUuFPHj4WBLa3uxtRaCsS3ffZBU66+rGNterzLBrfZGhzNAYitw3Isd9LMfbDod658wtIzm98l6hqJ+n6aWgxydY/eajbXqFAttTM7k+1LBJdr/HyMCY0EM2MObB4OcU215xtAysmRP0vqjf+lRLvH3A==~-1~-1~-1; bm_sv=5608A62D5E68D2ACA227FA9D6C9729B5~ynyChzuEsfL9Mar+1BiTImNN57zWtpLNnHKGhFxnjMsNaku8SRDMmlYKktjrS+U4SY77kyFEgludaTbRHJVb7W6U/mpXQkWO3M5LkI89zaf3XOSkr/lH7gN3TIjLq2NmfZQcr5ItH2wUXsI/JIXnGpNoOsmTpj3e9ASoOmTXXQQ=',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': f'https://www.tiktok.com/@{username_target}',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'close'
            }
            #req_get_id
            try:
                req_get_id = requests.get(url_get_id, headers=headers_get_id).text
                #Import ID
                id0 = re.findall('"userInfo":{"user":{"id":"(.*?)"', req_get_id)
                #Done Import ID
                id1 = "".join(id0)
                #def send_report():
                def send_report():
                    sleep = int(input('[?] Enter Sleep : '))
                    done = 0
                    error = 0
                    #url_send_report
                    url_send_report = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2F%40{username_target}%3F&root_referer=https:%2F%2Fwww.tiktok.com%2F%40e.2q&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=America%2FLos_Angeles&priority_region=SA&verifyFp=verify_kmxb0dd5_U5SMVNWR_g0Au_4r8J_9Qe3_NJxpQO88j1Pw&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6940688826462406145&tt-web-region=SA&uid=6951464259873604613'
                    #headers_send_report
                    headers_send_report = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'no-cache',
                        'content-length': '103',
                        'content-type': 'application/json',
                        'cookie': f'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; webapp_tiktok_lang=ar; tta_attr_id=0.1616499265.6942811476331593729; s_v_web_id=verify_kmxb0dd5_U5SMVNWR_g0Au_4r8J_9Qe3_NJxpQO88j1Pw; tt_csrf_token=biBAjWPswn1Ia8d_7rsdywQa; R6kq3TV7=AJL0p1x5AQAAgZ7UVUQ6Z_KKbbeh5V5rk1UaC0j4uVifRF8UZNUVrUJz9fFZ|1|0|bde1f506e2e120b4c97406a027a957d96a261126; csrf_session_id=f542d4c150684c8f8b565e56b620bff7; ak_bmsc=22C2B083F339CBE14339EFA65156A32656335E77BE330000BFCA9A6082EF1008~pl9qoJSA+vGmaFbpQTQUctlmE8lshSuY6YHoGK6eAFcwNGgFZsreTcrHNbxxGmpbl2GeyKL5276g5I/XQbSNpcwrr3cLsZ08fYr1T8IsmfB4yVD4pNbOvvocKs0Kwp4oGdquXtKten+dumIsbOYePAhDb4MopA6mBiXQ7IMKkZ66Gs9jhPn/1L7izxuAnlkvBQ2t4Ll3JgjK10tgMrmeooyS384GIBMU/9anOAEvzrh5c=; bm_sz=922FB4C8CA0E7C5EE7AAE96ED45A8D14~YAAQd14zVmmwGkJ5AQAAifunXAu6DUsNarpL0o3/MO2WbnFS6FTTWKwxn2twV02yxkLnXZhK4KuYsQdEvSzvN5Waphqt67i1QrSkqjqjrI+ud2Ipf8kP0aYBPU3F6aZBaTASUC/LPWyw6VSsJBdp2axybcksh9iN4tbe8ckxe0fS9e0HXMtG4zg14NKmCMF2; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQd14zVmqwGkJ5AQAAifunXAXD2Rm1wrf/kCpyHcjNt90XMNyT40T79i2Xiiv/+D7cSh+qO0hCvwfZPOdJLl1TZ/+70kjAkZhxQANKmbR1eG3hCoYziKZOVlLnIM4FvKCjI/8I0Ttyo2MPgy0k0Xd7aFV0JK9JNU0NBZTw4uTAjkpipxbcRFPw0Dzd6fxASkgbhUwGK866PwyfbVVffdeIqZ3USzyrTk6DR8lrU0M6tgsoRbx1/UY+Ue5MFQODr9n56Z6y/6LUuFPHj4WBLa3uxtRaCsS3ffZBU66+rGNterzLBrfZGhzNAYitw3Isd9LMfbDod658wtIzm98l6hqJ+n6aWgxydY/eajbXqFAttTM7k+1LBJdr/HyMCY0EM2MObB4OcU215xtAysmRP0vqjf+lRLvH3A==~-1~-1~-1; ttwid=1%7CwzXPnMZkgXiSYQk-tkK71Q8KqqRuVhoMRGQW1yNOtOE%7C1620760773%7C24fecb8fa91932b76e6480c16cb8392b7b1bfb21dd687901649d14a6ded3664e; sid_guard={sessionid}%7C1620760969%7C5184000%7CSat%2C+10-Jul-2021+19%3A22%3A49+GMT; uid_tt=7ade13dd61634ac8c0acf0504eb558b59373d907006ed6e825d82f5426c8c9e7; uid_tt_ss=7ade13dd61634ac8c0acf0504eb558b59373d907006ed6e825d82f5426c8c9e7; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; store-idc=maliva; store-country-code=pl; cmpl_token=AgQQAPORF-RMpbBGYU5-pd08-jPehXJPv4M0YP-2vw; MONITOR_WEB_ID=6940688826462406145; odin_tt=2d633d2f05bf5413d4279330ba74e7937da365b1ad0d6d01a219b6815756822efd2a5aaf337235a3adc8413c8903a81c158921702571c55cc51e94cd1f87726a33fc6573aa3dbaf3a184c6f346685d21; bm_sv=5608A62D5E68D2ACA227FA9D6C9729B5~ynyChzuEsfL9Mar+1BiTImNN57zWtpLNnHKGhFxnjMsNaku8SRDMmlYKktjrS+U4SY77kyFEgludaTbRHJVb7W6U/mpXQkWO3M5LkI89zafyBPRe7FzV/zaJVNirebe/+vLtXNlOYpEcIbBeY4r/GnE46suCVkZVdiP3+CfbrLw=',
                        'origin': 'https://www.tiktok.com',
                        'pragma': 'no-cache',
                        'referer': f'https://www.tiktok.com/@{username_target}?',
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'tt-csrf-token': 'biBAjWPswn1Ia8d_7rsdywQa',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                        'x-secsdk-csrf-token': '0001000000017fd8062e8dee2de712983b31249413824e9262c5ebf340ed4ef968f35674c08f167e198a92234268'
                    }
                    #data_send_report
                    data_send_report = {
                        'object_id': id1,
                        'owner_id': id1,
                        'reason': '3024',
                        'report_type': "user"
                    }
                    #req_send_report
                    #while True:
                    while True:
                        req_send_report = requests.post(url_send_report, json=data_send_report, headers=headers_send_report).text
                        if ('"statusCode":0,"errMsg":"نشكرك على ملاحظاتك"') in req_send_report:
                            #clear text
                            os.system("cls")
                            print(f'[{Fore.LIGHTMAGENTA_EX}Starting{Fore.RESET}]' + Fore.RESET)
                            Bb = Fore.LIGHTYELLOW_EX
                            print(Bb + """
        __  __ ____   _____  ____  _   _ 
        |  \/  |___ \ / ____|/ __ \| \ | |
        | \  / | __) | |  __| |  | |  \| |
        | |\/| ||__ <| | |_ | |  | | . ` |
        | |  | |___) | |__| | |__| | |\  |
        |_|  |_|____/ \_____|\____/|_| \_|
                            """, Fore.LIGHTGREEN_EX + "\n                  ( @_m3gon )",
                                  Fore.LIGHTBLUE_EX + "\n   (This tool is programmed by the programmer : @_m3gon)              \n",
                                  Fore.LIGHTYELLOW_EX + "                ( Report TikTok )\n\n" + Fore.RESET)
                            done +=1
                            print(f'\r[+] Done Report [{done}] | Error Report [{error}]', end='')
                            time.sleep(sleep)
                        else:
                            #clear Text
                            os.system("cls")
                            print(f'[{Fore.LIGHTMAGENTA_EX}Starting{Fore.RESET}]' + Fore.RESET)
                            Bb = Fore.LIGHTYELLOW_EX
                            print(Bb + """
        __  __ ____   _____  ____  _   _ 
        |  \/  |___ \ / ____|/ __ \| \ | |
        | \  / | __) | |  __| |  | |  \| |
        | |\/| ||__ <| | |_ | |  | | . ` |
        | |  | |___) | |__| | |__| | |\  |
        |_|  |_|____/ \_____|\____/|_| \_|
                            """, Fore.LIGHTGREEN_EX + "\n                  ( @_m3gon )",
                                  Fore.LIGHTBLUE_EX + "\n   (This tool is programmed by the programmer : @_m3gon)              \n",
                                  Fore.LIGHTYELLOW_EX + "                ( Report TikTok )\n\n" + Fore.RESET)
                            print(f'[{Fore.LIGHTMAGENTA_EX}Starting{Fore.RESET}]' + Fore.RESET)
                            print('')
                            error +=1
                            print(f'\r[+] Done Report [{done}] | Error Report [{error}]', end='')
                            time.sleep(sleep)
                send_report()
            except:
                print('[-] Error get id target')
                time.sleep(10)
        get_id_target()
    else:
        print(Fore.LIGHTRED_EX+'[-] Failed Login')
        time.sleep(10)
check_sessionid_true_or_error()
