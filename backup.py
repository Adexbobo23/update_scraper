from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon import TelegramClient
from telethon.errors import PeerFloodError, FloodWaitError, ChatWriteForbiddenError, ChatAdminRequiredError
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = f'{lg}[{w}i{lg}]{rs}'
error = f'{lg}[{r}!{lg}]{rs}'
success = f'{w}[{lg}*{w}]{rs}'
INPUT = f'{lg}[{cy}~{lg}]{rs}'
plus = f'{w}[{lg}+{w}]{rs}'
minus = f'{w}[{lg}-{w}]{rs}'

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    '░██████╗███████╗████████╗██╗░░░██╗██████╗░',
    '██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗',
    '╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝',
    '░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░',
    '██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░',
    '╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░'
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    print('Contact below address for get premium script')
    print(f'{lg}Version: {w}2.0{lg}')
    print(f'{lg}Telegram: {w}@Scrapeleet{lg}')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def manager():
    while True:
        clr()
        banner()
        print(f'\n{lg}[1] Add new accounts{n}')
        print(f'{lg}[2] Filter all banned accounts{n}')
        print(f'{lg}[3] Delete specific accounts{n}')
        print(f'{lg}[4] Update your Script{n}')
        print(f'{lg}[5] Display All Accounts{n}')
        print(f'{lg}[6] Quit{n}')
        a = int(input('\nEnter your choice: '))

        if a == 1:
            new_accs = []
            with open('vars.txt', 'ab') as g:
                number_to_add = int(input(f'\n{lg} [~] Enter How Many Accounts You Want To Add: {r}'))
                for _ in range(number_to_add):
                    phone_number = str(input(f'\n{lg} [~] Enter Phone Number With Country Code: {r}'))
                    parsed_number = ''.join(phone_number.split())
                    pickle.dump([parsed_number], g)
                    new_accs.append(parsed_number)
                print(f'\n{lg} [i] Saved all accounts in vars.txt')
                clr()
                print(f'\n{lg} [*] Logging in from new accounts\n')
                for number in new_accs:
                    c = TelegramClient(f'sessions/{number}', 3910389, '86f861352f0ab76a251866059a6adbd6')
                    try:
                        while True:
                            try:
                                c.start(number)
                                print(f'{lg}[+] Login successful for {number}')
                                break  # Exit the loop once the login is successful
                            except Exception as e:
                                if 'code' in str(e).lower():
                                    print(f'{error} Incorrect code entered. Please try again for {number}.')
                                else:
                                    print(f'{error} An error occurred: {e}')
                                    break  # Break if the error is not related to the code
                    except Exception as e:
                        print(f'{error} Unable to login with {number}. Error: {e}')
                    finally:
                        c.disconnect()
                input(f'\n Press enter to go to the main menu...')
            g.close()
        elif a == 2:
            accounts = []
            banned_accs = []
            with open('vars.txt', 'rb') as h:
                while True:
                    try:
                        accounts.append(pickle.load(h))
                    except EOFError:
                        break
            if not accounts:
                print(f'{r}[!] There are no accounts! Please add some and retry')
                sleep(3)
            else:
                for account in accounts:
                    phone = str(account[0])
                    client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                    client.connect()
                    if not client.is_user_authorized():
                        try:
                            client.send_code_request(phone)
                            print(f'{lg}[+] {phone} is not banned{n}')
                        except PhoneNumberBannedError:
                            print(r + phone + ' is banned!' + n)
                            banned_accs.append(account)
                if not banned_accs:
                    print(f'{lg}Congrats! No banned accounts')
                else:
                    for m in banned_accs:
                        accounts.remove(m)
                    with open('vars.txt', 'wb') as k:
                        for a in accounts:
                            Phone = a[0]
                            pickle.dump([Phone], k)
                    k.close()
                    print(f'{lg}[i] All banned accounts removed{n}')
                input('\nPress enter to goto main menu...')

        elif a == 3:
            accs = []
            with open('vars.txt', 'rb') as f:
                while True:
                    try:
                        accs.append(pickle.load(f))
                    except EOFError:
                        break
            print(f'{lg}[i] Choose an account to delete\n')
            for i, acc in enumerate(accs):
                print(f'{lg}[{i}] {acc[0]}{n}')
            index = int(input(f'\n{lg}[+] Enter a choice: {n}'))
            phone = str(accs[index][0])
            session_file = f'{phone}.session'
            if os.name == 'nt':
                os.system(f'del sessions\\{session_file}')
            else:
                os.system(f'rm sessions/{session_file}')
            del accs[index]
            with open('vars.txt', 'wb') as f:
                for account in accs:
                    pickle.dump(account, f)
                print(f'\n{lg}[+] Account Deleted{n}')
                input(f'\nPress enter to goto main menu...')

        elif a == 4:
            print(f'\n{lg}[i] Checking for updates...')
            try:
                version = requests.get('https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/version.txt')
            except:
                print(f'{r} You are not connected to the internet')
                print(f'{r} Please connect to the internet and retry')
                exit()
            if float(version.text) > 2.0:
                prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
                if prompt in {'y', 'yes', 'Y'}:
                    print(f'{lg}[i] Downloading updates...')
                    if os.name == 'nt':
                        os.system('del add.py')
                        os.system('del manager.py')
                    else:
                        os.system('rm add.py')
                        os.system('rm manager.py')
                    os.system('curl -l -O https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/add.py')
                    os.system('curl -l -O https://raw.githubusercontent.com/saifalisew1508/Telegram-Members-Adder/main/manager.py')
                    print(f'{lg}[*] Updated to version: {version.text}')
                    input('Press enter to exit...')
                    exit()
                else:
                    print(f'{lg}[!] Update aborted.')
                    input('Press enter to goto main menu...')
            else:
                print(f'{lg}[i] Your Scrapeleet Telegram-Members-Adder is already up to date')
                input('Press enter to goto main menu...')

        elif a == 5:
            accs = []
            with open('vars.txt', 'rb') as f:
                while True:
                    try:
                        accs.append(pickle.load(f))
                    except EOFError:
                        break
            print(f'\n{cy}')
            print(f'\tList Of Phone Numbers Are')
            print('==========================================================')
            for z in accs:
                print(f'\t{z[0]}')
            print('==========================================================')
            input('\nPress enter to goto main menu')

        elif a == 6:
            clr()
            banner()
            exit()


def automation():
    def banner():
        # fancy logo
        b = [
            '░█████╗░██████╗░██████╗░███████╗██████╗░',
            '██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',
            '███████║██║░░██║██║░░██║█████╗░░██████╔╝',
            '██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗',
            '██║░░██║██████╔╝██████╔╝███████╗██║░░██║',
            '╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝'
        ]
        for char in b:
            print(f'{random.choice(colors)}{char}{rs}')
        print('Contact below address for get premium script')
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@adexbobo23{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    # function to clear screen
    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    accounts = []
    f = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(f))
        except EOFError:
            break

    # create sessions(if any) and check for any banned accounts
    # TODO: Remove code input(just to check if an account is banned)
    print('\n' + info + lg + ' Checking for banned accounts...' + rs)
    for a in accounts:
        phn = a[0]
        print(f'{plus}{grey} Checking {lg}{phn}')
        clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        clnt.connect()
        banned = []
        if not clnt.is_user_authorized():
            try:
                clnt.send_code_request(phn)
                print('OK')
            except PhoneNumberBannedError:
                print(f'{error} {w}{phn} {r}is banned!{rs}')
                banned.append(a)
        for z in banned:
            accounts.remove(z)
            print(info + lg + ' Banned account removed[Remove permanently using manager.py]' + rs)
        time.sleep(0.5)
        clnt.disconnect()

    print(f'{info} Sessions created!')
    clr()
    banner()

    # func to log scraping details(link of the grp to scrape and current index) in order to resume later
    def log_status(scraped, index):
        with open('status.dat', 'wb') as f:
            pickle.dump([scraped, int(index)], f)
            f.close()
        print(f'{info}{lg} Session stored in {w}status.dat{lg}')

    def exit_window():
        input(f'\n{cy} Press enter to exit...')
        clr()
        banner()
        sys.exit()

    # read user details
    try:
        # request to resume adding
        with open('status.dat', 'rb') as f:
            status = pickle.load(f)
            f.close()
            lol = input(f'{INPUT}{cy} Resume scraping members from {w}{status[0]}{lg}? [y/n]: {r}')
            if 'y' in lol:
                scraped_grp = status[0]
                index = int(status[1])
            else:
                if os.name == 'nt':
                    os.system('del status.dat')
                else:
                    os.system('rm status.dat')
                scraped_grp = input(f'{INPUT}{cy} Public/Private group url link to scrape members: {r}')
                index = 0
    except:
        scraped_grp = input(f'{INPUT}{cy} Public/Private group url link to scrape members: {r}')
        index = 0

    # load all the accounts(phonenumbers)
    accounts = []
    f = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(f))
        except EOFError:
            break

    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want Use In Adding: {r}'))
    print(f'{info}{cy} Choose an option{lg}')
    print(f'{cy}[0]{lg} Add to public group')
    print(f'{cy}[1]{lg} Add to private group')
    choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

    if choice == 0:
        target = str(input(f'{INPUT}{cy} Enter public group url link: {r}'))
    else:
        target = str(input(f'{INPUT}{cy} Enter private group url link: {r}'))

    print(f'{grey}_' * 50)
    status_choice = str(input(f'{INPUT}{cy} Do you wanna add active members?[y/n]: {r}'))
    to_use = list(accounts[:number_of_accs])
    for l in to_use: accounts.remove(l)
    with open('vars.txt', 'wb') as f:
        for a in accounts:
            pickle.dump(a, f)
        for ab in to_use:
            pickle.dump(ab, f)
        f.close()

    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request{w}[{lg}0 for None, I suggest entering 30 to add members properly{w}]: {r}'))
    print(f'{info}{lg} Joining group from {w}{number_of_accs} accounts...')
    print(f'{grey}-' * 50)
    print(f'{success}{lg} -- Adding members from {w}{len(to_use)}{lg} account(s) --')
    adding_status = 0
    approx_members_count = 0

    for acc in to_use:
        stop = index + 60
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
        c.start(acc[0])
        acc_name = c.get_me().first_name
        try:
            if '/joinchat/' in scraped_grp:
                g_hash = scraped_grp.split('/joinchat/')[1]
                try:
                    c(ImportChatInviteRequest(g_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
                except UserAlreadyParticipantError:
                    pass
            else:
                c(JoinChannelRequest(scraped_grp))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
            scraped_grp_entity = c.get_entity(scraped_grp)
            if choice == 0:
                c(JoinChannelRequest(target))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to add')
                target_entity = c.get_entity(target)
                target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
            else:
                try:
                    grp_hash = target.split('/joinchat/')[1]
                    c(ImportChatInviteRequest(grp_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to add')
                except UserAlreadyParticipantError:
                    pass
                target_entity = c.get_entity(target)
                target_details = target_entity
        except Exception as e:
            print(f'{error}{r} User: {cy}{acc_name}{lg} -- Failed to join group')
            print(f'{error} {r}{e}')
            continue
        print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Retrieving entities...')
        c.get_dialogs()
        try:
            members = []
            members = c.get_participants(scraped_grp_entity, aggressive=False)
        except Exception as e:
            print(f'{error}{r} Couldn\'t scrape members')
            print(f'{error}{r} {e}')
            continue
        approx_members_count = len(members)
        assert approx_members_count != 0
        if index >= approx_members_count:
            print(f'{error}{lg} No members to add!')
            continue
        print(f'{info}{lg} Start: {w}{index}')
        adding_status = 0
        peer_flood_status = 0
        for user in members[index:stop]:
            index += 1
            if user.bot:
                continue
            try:
                c(InviteToChannelRequest(target_details, [user]))
                print(f'{success}{lg} User: {cy}{acc_name}{lg} -- Added member {cy}{user.username}')
                time.sleep(sleep_time)
                adding_status += 1
            except UserAlreadyParticipantError:
                print(f'{info}{cy} User: {cy}{acc_name}{lg} -- User {cy}{user.username} already added!{rs}')
            except UserPrivacyRestrictedError:
                print(f'{info}{cy} User: {cy}{acc_name}{lg} -- User {cy}{user.username} has privacy restrictions!{rs}')
            except ChatWriteForbiddenError:
                print(f'{info}{cy} User: {cy}{acc_name}{lg} -- No permission to write in the group!{rs}')
            except PeerFloodError:
                peer_flood_status += 1
                print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Peer flood error...{rs}')
                if peer_flood_status == 5:
                    print(f'{info}{lg} You have been rate-limited, waiting for 60 seconds...{rs}')
                    time.sleep(60)
                    continue
            except ChatAdminRequiredError:
                print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Admin permission required to add members!{rs}')
            except FloodWaitError:
                print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Flood wait error! Sleeping for 15 seconds...{rs}')
                time.sleep(15)
            except Exception as e:
                print(f'{error}{r} Error: {e}')
                time.sleep(5)
                continue
            if stop == approx_members_count or index >= approx_members_count:
                break
        if adding_status > 0:
            log_status(scraped_grp, index)
            print(f'{info}{lg} Successfully added {w}{adding_status} members{lg} from account {w}{acc_name}')
        c.disconnect()
        print(f'{grey}-' * 50)

    print(f'{info}{lg} Finished adding members!{rs}')



# Message Moving

def move_messages():
    def banner():
        # fancy logo
        b = [
            '░█████╗░██████╗░██████╗░███████╗██████╗░',
            '██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',
            '███████║██║░░██║██║░░██║█████╗░░██████╔╝',
            '██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗',
            '██║░░██║██████╔╝██████╔╝███████╗██║░░██║',
            '╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝'
        ]
        for char in b:
            print(f'{random.choice(colors)}{char}{rs}')
        print('Contact below address for get premium script')
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@adexbobo23{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    # function to clear screen
    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    accounts = []
    f = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(f))
        except EOFError:
            break

    # create sessions(if any) and check for any banned accounts
    print('\n' + info + lg + ' Checking for banned accounts...' + rs)
    banned = []
    for a in accounts:
        phn = a[0]
        print(f'{plus}{grey} Checking {lg}{phn}')
        clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        clnt.connect()
        if not clnt.is_user_authorized():
            try:
                clnt.send_code_request(phn)
                print('OK')
            except:
                print(f'{error} {w}{phn} {r}is banned!{rs}')
                banned.append(a)
        time.sleep(0.5)
        clnt.disconnect()

    for z in banned:
        accounts.remove(z)
        print(info + lg + ' Banned account removed' + rs)

    print(f'{info} Sessions created!')
    clr()
    banner()

    # read user details
    try:
        # request to resume adding
        with open('status.dat', 'rb') as f:
            status = pickle.load(f)
            f.close()
            lol = input(f'{INPUT}{cy} Resume moving messages from {w}{status[0]}{lg}? [y/n]: {r}')
            if 'y' in lol:
                scraped_grp = status[0]
                index = int(status[1])
            else:
                if os.name == 'nt':
                    os.system('del status.dat')
                else:
                    os.system('rm status.dat')
                scraped_grp = input(f'{INPUT}{cy} Public/Private group url link to scrape messages: {r}')
                index = 0
    except:
        scraped_grp = input(f'{INPUT}{cy} Public/Private group url link to scrape messages: {r}')
        index = 0

    # load all the accounts(phonenumbers)
    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want Use In Moving: {r}'))
    print(f'{info}{cy} Choose an option{lg}')
    print(f'{cy}[0]{lg} Move to public group')
    print(f'{cy}[1]{lg} Move to private group')
    choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

    if choice == 0:
        target = str(input(f'{INPUT}{cy} Enter public group url link: {r}'))
    else:
        target = str(input(f'{INPUT}{cy} Enter private group url link: {r}'))

    print(f'{grey}_' * 50)
    to_use = list(accounts[:number_of_accs])
    for l in to_use: accounts.remove(l)
    with open('vars.txt', 'wb') as f:
        for a in accounts:
            pickle.dump(a, f)
        for ab in to_use:
            pickle.dump(ab, f)
        f.close()

    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request{w}[{lg}0 for None, I suggest entering 30{w}]: {r}'))
    print(f'{info}{lg} Moving messages from {w}{number_of_accs} accounts...')
    print(f'{grey}-' * 50)

    for acc in to_use:
        stop = index + 60
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
        c.start(acc[0])
        acc_name = c.get_me().first_name
        try:
            if '/joinchat/' in scraped_grp:
                g_hash = scraped_grp.split('/joinchat/')[1]
                try:
                    c(ImportChatInviteRequest(g_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
                except:
                    pass
            else:
                c(JoinChannelRequest(scraped_grp))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
            scraped_grp_entity = c.get_entity(scraped_grp)
            if choice == 0:
                c(JoinChannelRequest(target))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to move messages to')
                target_entity = c.get_entity(target)
                target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
            else:
                try:
                    grp_hash = target.split('/joinchat/')[1]
                    c(ImportChatInviteRequest(grp_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to move messages to')
                except:
                    pass
                target_entity = c.get_entity(target)
                target_details = target_entity
        except Exception as e:
            print(f'{error}{r} User: {cy}{acc_name}{lg} -- Failed to join group')
            print(f'{error} {r}{e}')
            continue
        print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Retrieving entities...')
        c.get_dialogs()
        try:
            messages = c.get_messages(scraped_grp_entity, limit=100)  # Get last 100 messages
        except Exception as e:
            print(f'{error}{r} Couldn\'t retrieve messages')
            print(f'{error}{r} {e}')
            continue
        
        for msg in messages:
            try:
                c(SendMessageRequest(target_details, msg.text))
                print(f'{success}{lg} User: {cy}{acc_name}{lg} -- Moved message: {cy}{msg.text}')
                time.sleep(sleep_time)
            except Exception as e:
                print(f'{error}{r} Error moving message: {e}')
                continue
        
        if stop == len(messages) or index >= len(messages):
            break
        index += 1
        c.disconnect()

    print(f'{info}{lg} Finished moving messages!{rs}')


# Hidden Groups Members Adder

def hidden_members():
    def banner():
        # fancy logo
        b = [
            '░█████╗░██████╗░██████╗░███████╗██████╗░',
            '██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',
            '███████║██║░░██║██║░░██║█████╗░░██████╔╝',
            '██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗',
            '██║░░██║██████╔╝██████╔╝███████╗██║░░██║',
            '╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝'
        ]
        for char in b:
            print(f'{random.choice(colors)}{char}{rs}')
        print('Contact below address for get premium script')
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@adexbobo23{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    # function to clear screen
    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    accounts = []
    f = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(f))
        except EOFError:
            break

    # create sessions(if any) and check for any banned accounts
    # TODO: Remove code input(just to check if an account is banned)
    print('\n' + info + lg + ' Checking for banned accounts...' + rs)
    for a in accounts:
        phn = a[0]
        print(f'{plus}{grey} Checking {lg}{phn}')
        clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        clnt.connect()
        banned = []
        if not clnt.is_user_authorized():
            try:
                clnt.send_code_request(phn)
                print('OK')
            except PhoneNumberBannedError:
                print(f'{error} {w}{phn} {r}is banned!{rs}')
                banned.append(a)
        for z in banned:
            accounts.remove(z)
            print(info + lg + ' Banned account removed[Remove permanently using manager.py]' + rs)
        time.sleep(0.5)
        clnt.disconnect()

    print(f'{info} Sessions created!')
    clr()
    banner()

    # func to log scraping details(link of the grp to scrape and current index) in order to resume later
    def log_status(scraped, index):
        with open('status.dat', 'wb') as f:
            pickle.dump([scraped, int(index)], f)
            f.close()
        print(f'{info}{lg} Session stored in {w}status.dat{lg}')

    def exit_window():
        input(f'\n{cy} Press enter to exit...')
        clr()
        banner()
        sys.exit()

    # read user details
    try:
        # request to resume adding
        with open('status.dat', 'rb') as f:
            status = pickle.load(f)
            f.close()
            lol = input(f'{INPUT}{cy} Resume scraping hidden members from {w}{status[0]}{lg}? [y/n]: {r}')
            if 'y' in lol:
                scraped_grp = status[0]
                index = int(status[1])
            else:
                if os.name == 'nt':
                    os.system('del status.dat')
                else:
                    os.system('rm status.dat')
                scraped_grp = input(f'{INPUT}{cy} Public/Private group url link to scrape members: {r}')
                index = 0
    except:
        scraped_grp = input(f'{INPUT}{cy} Public/Private group url link to scrape hidden members: {r}')
        index = 0

    # load all the accounts(phonenumbers)
    accounts = []
    f = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(f))
        except EOFError:
            break

    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want Use In Adding: {r}'))
    print(f'{info}{cy} Choose an option{lg}')
    print(f'{cy}[0]{lg} Add to public group')
    print(f'{cy}[1]{lg} Add to private group')
    choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

    if choice == 0:
        target = str(input(f'{INPUT}{cy} Enter public group url link: {r}'))
    else:
        target = str(input(f'{INPUT}{cy} Enter private group url link: {r}'))

    print(f'{grey}_' * 50)
    status_choice = str(input(f'{INPUT}{cy} Do you wanna add active hidden members?[y/n]: {r}'))
    to_use = list(accounts[:number_of_accs])
    for l in to_use: accounts.remove(l)
    with open('vars.txt', 'wb') as f:
        for a in accounts:
            pickle.dump(a, f)
        for ab in to_use:
            pickle.dump(ab, f)
        f.close()

    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request{w}[{lg}0 for None, I suggest entering 30 to add hidden members properly{w}]: {r}'))
    print(f'{info}{lg} Joining group from {w}{number_of_accs} accounts...')
    print(f'{grey}-' * 50)
    print(f'{success}{lg} -- Adding hidden members from {w}{len(to_use)}{lg} account(s) --')
    adding_status = 0
    approx_members_count = 0

    for acc in to_use:
        stop = index + 60
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
        c.start(acc[0])
        acc_name = c.get_me().first_name
        try:
            if '/joinchat/' in scraped_grp:
                g_hash = scraped_grp.split('/joinchat/')[1]
                try:
                    c(ImportChatInviteRequest(g_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
                except UserAlreadyParticipantError:
                    pass
            else:
                c(JoinChannelRequest(scraped_grp))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
            scraped_grp_entity = c.get_entity(scraped_grp)
            if choice == 0:
                c(JoinChannelRequest(target))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to add')
                target_entity = c.get_entity(target)
                target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
            else:
                try:
                    grp_hash = target.split('/joinchat/')[1]
                    c(ImportChatInviteRequest(grp_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to add')
                except UserAlreadyParticipantError:
                    pass
                target_entity = c.get_entity(target)
                target_details = target_entity
        except Exception as e:
            print(f'{error}{r} User: {cy}{acc_name}{lg} -- Failed to join group')
            print(f'{error} {r}{e}')
            continue
        print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Retrieving entities...')
        c.get_dialogs()
        try:
            members = []
            members = c.get_participants(scraped_grp_entity, aggressive=False)
        except Exception as e:
            print(f'{error}{r} Couldn\'t scrape members')
            print(f'{error}{r} {e}')
            continue
        approx_members_count = len(members)
        assert approx_members_count != 0
        if index >= approx_members_count:
            print(f'{error}{lg} No members to add!')
            continue
        print(f'{info}{lg} Start: {w}{index}')
        adding_status = 0
        peer_flood_status = 0
        for user in members[index:stop]:
            index += 1
            if user.bot:
                continue
            try:
                c(InviteToChannelRequest(target_details, [user]))
                print(f'{success}{lg} User: {cy}{acc_name}{lg} -- Added member {cy}{user.username}')
                time.sleep(sleep_time)
                adding_status += 1
            except UserAlreadyParticipantError:
                print(f'{info}{cy} User: {cy}{acc_name}{lg} -- User {cy}{user.username} already added!{rs}')
            except UserPrivacyRestrictedError:
                print(f'{info}{cy} User: {cy}{acc_name}{lg} -- User {cy}{user.username} has privacy restrictions!{rs}')
            except ChatWriteForbiddenError:
                print(f'{info}{cy} User: {cy}{acc_name}{lg} -- No permission to write in the group!{rs}')
            except PeerFloodError:
                peer_flood_status += 1
                print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Peer flood error...{rs}')
                if peer_flood_status == 5:
                    print(f'{info}{lg} You have been rate-limited, waiting for 60 seconds...{rs}')
                    time.sleep(60)
                    continue
            except ChatAdminRequiredError:
                print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Admin permission required to add members!{rs}')
            except FloodWaitError:
                print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Flood wait error! Sleeping for 15 seconds...{rs}')
                time.sleep(15)
            except Exception as e:
                print(f'{error}{r} Error: {e}')
                continue
            if stop == approx_members_count or index >= approx_members_count:
                break
        if adding_status > 0:
            log_status(scraped_grp, index)
            print(f'{info}{lg} Successfully added {w}{adding_status} hidden members{lg} from account {w}{acc_name}')
        c.disconnect()
        print(f'{grey}-' * 50)

    print(f'{info}{lg} Finished adding members!{rs}')

# Token Verification Code

import requests
import os

# URL of the Django server's verify token endpoint
VERIFY_TOKEN_URL = "https://scrapeleet.com/verify-token/"
TOKEN_FILE = "token.txt"  # File to store the verified token

def verify_token(token):
    """Verifies the token with the Django backend."""
    response = requests.post(VERIFY_TOKEN_URL, json={'token': token})
    if response.status_code == 200:
        data = response.json()
        return data.get('status') == 'valid', data.get('user_id')
    else:
        return False, None

def load_token():
    """Loads the token from the token file if it exists."""
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as file:
            return file.read().strip()  
    return None

def save_token(token):
    """Saves the token to the token file."""
    with open(TOKEN_FILE, 'w') as file:
        file.write(token)  # Write the token to the file


from colorama import Fore

# Define colors
r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]

# Define formatted messages
info = f'{lg}[{w}i{lg}]{rs}'
error = f'{lg}[{r}!{lg}]{rs}'
success = f'{w}[{lg}*{w}]{rs}'
INPUT = f'{lg}[{cy}~{lg}]{rs}'
plus = f'{w}[{lg}+{w}]{rs}'
minus = f'{w}[{lg}-{w}]{rs}'

def main_menu():
    token = load_token()

    if token is None:
        token = input(lg + "[+] Enter your purchase token: ")
    else:
        is_valid, user_id = verify_token(token)
        if not is_valid:
            print(r + "[!] Invalid or expired token. Please purchase a valid token to continue.")
            exit(1)
        print(lg + f"[+] Loaded token verified for user ID: {user_id}. Access granted to the scraper.")
    
    is_valid, user_id = verify_token(token)
    if is_valid:
        save_token(token)
    else:
        print(r + "[!] Invalid or expired token. Please purchase a valid token to continue.")
        exit(1)

    """Display the main menu with options."""
    menu = f"""
{cy}╔════════════════════════════════════╗
{cy}║          {lg}Main Menu{cy}           ║
{cy}╚════════════════════════════════════╝
{lg}1.{rs} Manage Account
{lg}2.{rs} Automate Scraping and Members Adding
{lg}3.{rs} Automate Scraping and Hidden Members Adding
{lg}4.{rs} Move Message From Group to Group
"""
    print(menu)
    choice = input(f'\n{INPUT}{cy} Select an action: {rs}')

    if choice == '1':
        manager()
    elif choice == '2':
        while True:
            automation()
    elif choice == '3':
        while True:
            hidden_members()
    elif choice == '4':
        move_messages()
    else:
        print(f'{error} {r}Invalid choice! Please select a valid option.{rs}')

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f'\n{error} {r}Operation interrupted by the user. Exiting...{rs}')
