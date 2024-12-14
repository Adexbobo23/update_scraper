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
            existing_numbers = set()
            
            # Load existing numbers from vars.txt
            try:
                with open('vars.txt', 'rb') as file:
                    while True:
                        try:
                            existing_numbers.update(pickle.load(file))
                        except EOFError:
                            break
            except FileNotFoundError:
                pass  # File doesn't exist yet, so no numbers to load

            with open('vars.txt', 'ab') as g:
                # Loop to ensure user enters a valid integer for the number of accounts to add
                while True:
                    try:
                        number_to_add = int(input(f'\n{lg} [~] Enter How Many Accounts You Want To Add: {r}'))
                        if number_to_add <= 0:
                            print(f'{error} Please enter a positive number.')
                            continue
                        break
                    except ValueError:
                        print(f'{error} Invalid input. Please enter a valid number.')

                for _ in range(number_to_add):
                    while True:
                        phone_number = input(f'\n{lg} [~] Enter Phone Number With Country Code: {r}').strip()
                        if phone_number.isdigit():
                            parsed_number = ''.join(phone_number.split())
                            if parsed_number in existing_numbers:
                                print(f'{error} This phone number already exists in the file.')
                                continue
                            pickle.dump([parsed_number], g)
                            new_accs.append(parsed_number)
                            existing_numbers.add(parsed_number)
                            break  # Exit the loop if a valid phone number is entered
                        else:
                            print(f'{error} Please enter a valid phone number with only digits.')

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
                version_url = 'https://raw.githubusercontent.com/Adexbobo23/scrapeleet_update/main/version.txt'
                version = requests.get(version_url).text.strip()
            except Exception as e:
                print(f'{r} You are not connected to the internet or the server is unavailable.')
                print(f'{r} Error: {e}')
                print(f'{r} Please connect to the internet and retry.')
                exit()

            local_version = 2.0  # Update this to your script's current version
            if float(version) > local_version:
                prompt = str(input(f'{lg}[~] Update available [Version {version}]. Download? [y/n]: {r}')).strip().lower()
                if prompt in {'y', 'yes'}:
                    print(f'{lg}[i] Downloading updates...')
                    try:
                        file_url = 'https://raw.githubusercontent.com/Adexbobo23/scrapeleet_update/main/main.py'
                        response = requests.get(file_url)
                        response.raise_for_status()  # Check for HTTP request errors

                        # Backup existing file (overwrite if the backup already exists)
                        if os.path.exists('main.py'):
                            os.replace('main.py', 'main.py.bak')

                        # Save the updated file with UTF-8 encoding
                        with open('main.py', 'w', encoding='utf-8') as f:
                            f.write(response.text)
                        
                        print(f'{lg}[+] Successfully updated main.py to version {version}.')
                        input('Press enter to exit...')
                        exit()
                    except Exception as e:
                        print(f'{r}[!] Failed to update main.py. Error: {e}')
                        # Restore backup if update fails
                        if os.path.exists('main.py.bak'):
                            os.replace('main.py.bak', 'main.py')
                        print(f'{r}[!] Reverted to the previous version of main.py.')
                        input('Press enter to go to the main menu...')
                else:
                    print(f'{lg}[!] Update aborted.')
                    input('Press enter to go to the main menu...')
            else:
                print(f'{lg}[i] Your Telegram-Members-Adder is already up to date.')
                input('Press enter to go to the main menu...')


        # elif a == 4:
        #     print(f'\n{lg}[i] Checking for updates...')
        #     try:
        #         version = requests.get('https://raw.githubusercontent.com/Adexbobo23/scrapeleet_update/main/version.txt')
        #     except:
        #         print(f'{r} You are not connected to the internet')
        #         print(f'{r} Please connect to the internet and retry')
        #         exit()
        #     if float(version.text) > 2.0:
        #         prompt = str(input(f'{lg}[~] Update available[Version {version.text}]. Download?[y/n]: {r}'))
        #         if prompt in {'y', 'yes', 'Y'}:
        #             print(f'{lg}[i] Downloading updates...')
        #             if os.name == 'nt':
        #                 os.system('del add.py')
        #                 os.system('del manager.py')
        #             else:
        #                 os.system('rm add.py')
        #                 os.system('rm manager.py')
        #             os.system('curl -l -O https://raw.githubusercontent.com/Adexbobo23/scrapeleet_update/main/add.py')
        #             os.system('curl -l -O https://raw.githubusercontent.com/Adexbobo23/scrapeleet_update/main/manager.py')
        #             print(f'{lg}[*] Updated to version: {version.text}')
        #             input('Press enter to exit...')
        #             exit()
        #         else:
        #             print(f'{lg}[!] Update aborted.')
        #             input('Press enter to goto main menu...')
        #     else:
        #         print(f'{lg}[i] Your Scrapeleet Telegram-Members-Adder is already up to date')
        #         input('Press enter to goto main menu...')

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

from telethon.sync import TelegramClient
from telethon.errors import UserAlreadyParticipantError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import pickle
import time
import os
import sys

def auto_join_group():
    def banner():
        b = [
            '░█████╗░██████╗░██████╗░███████╗██████╗░',
            '██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',
            '███████║██║░░██║██║░░██║█████╗░░██████╔╝',
            '██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗',
            '██║░░██║██████╔╝██████╔╝███████╗██║░░██║',
            '╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝'
        ]
        for char in b:
            print(char)
        print('Contact below address for get premium script')
        print('Version: 2.0 | GitHub: @Scrapeleet')
        print('Telegram: @Scrapeleet | Instagram: @Scrapeleet\n')

    def load_accounts():
        accounts = []
        with open('vars.txt', 'rb') as f:
            while True:
                try:
                    accounts.append(pickle.load(f))
                except EOFError:
                    break
        return accounts

    group_link = 'https://t.me/scrapeleet'
    accounts = load_accounts()
    print(f'Total accounts: {len(accounts)}')

    for account in accounts:
        phone = account[0]
        client = TelegramClient(f'sessions/{phone}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        client.connect()
        
        if not client.is_user_authorized():
            print(f'{phone} is not authorized. Skipping...')
            continue

        try:
            #print(f'Joining group with account {phone}...')
            if '/joinchat/' in group_link:
                invite_hash = group_link.split('/joinchat/')[1]
                client(ImportChatInviteRequest(invite_hash))
            else:
                client(JoinChannelRequest(group_link))
            # print(f'Successfully joined the group with account {phone}')
        except UserAlreadyParticipantError:
            print(f'Account {phone} is already a participant.')
        except Exception as e:
            print(f'Failed to join group with account {phone}: {e}')
        finally:
            client.disconnect()
        time.sleep(2)  # Small delay between account joins

    print('All accounts have been processed.')



def auto_join_group_smmleet():
    def banner():
        b = [
            '░█████╗░██████╗░██████╗░███████╗██████╗░',
            '██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',
            '███████║██║░░██║██║░░██║█████╗░░██████╔╝',
            '██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗',
            '██║░░██║██████╔╝██████╔╝███████╗██║░░██║',
            '╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝'
        ]
        for char in b:
            print(char)
        print('Contact below address for get premium script')
        print('Version: 2.0 | GitHub: @Scrapeleet')
        print('Telegram: @Scrapeleet | Instagram: @Scrapeleet\n')

    def load_accounts():
        accounts = []
        with open('vars.txt', 'rb') as f:
            while True:
                try:
                    accounts.append(pickle.load(f))
                except EOFError:
                    break
        return accounts

    group_link = 'https://t.me/smmleet'
    accounts = load_accounts()
    print(f'Total accounts: {len(accounts)}')

    for account in accounts:
        phone = account[0]
        client = TelegramClient(f'sessions/{phone}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        client.connect()
        
        if not client.is_user_authorized():
            print(f'{phone} is not authorized. Skipping...')
            continue

        try:
            #print(f'Joining group with account {phone}...')
            if '/joinchat/' in group_link:
                invite_hash = group_link.split('/joinchat/')[1]
                client(ImportChatInviteRequest(invite_hash))
            else:
                client(JoinChannelRequest(group_link))
            # print(f'Successfully joined the group with account {phone}')
        except UserAlreadyParticipantError:
            print(f'Account {phone} is already a participant.')
        except Exception as e:
            print(f'Failed to join group with account {phone}: {e}')
        finally:
            client.disconnect()
        time.sleep(2)  # Small delay between account joins

    print('All accounts have been processed.')




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
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
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
    print('Adding Account To Scrapeleet Channels in case you wanna speak to us')
    auto_join_group()
    print('All Account added successfully to Scrapeleet group\n')

    print("Loading and Checking for verifications")
    time.sleep(5)
    auto_join_group_smmleet()

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
        target = str(input(f'{INPUT}{cy} Enter public group url link to add members: {r}'))
    else:
        target = str(input(f'{INPUT}{cy} Enter private group url link to add members: {r}'))

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


# Online Members
from telethon.tl.types import UserStatusOnline 

def automation_online_only():
    def banner():
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
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # Initialization and user input
    accounts = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    scraped_grp = input(f'{INPUT}{cy} Public/Private group URL to scrape online members: {r}')
    target_grp = input(f'{INPUT}{cy} Enter group URL to add members: {r}')
    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request: {r}'))

    for acc in accounts:
        client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        client.connect()
        client.start(acc[0])
        print(f'{info}{lg} Logged in as {client.get_me().first_name}')

        # Joining the source group
        try:
            if '/joinchat/' in scraped_grp:
                invite_hash = scraped_grp.split('/joinchat/')[1]
                client(ImportChatInviteRequest(invite_hash))
            else:
                client(JoinChannelRequest(scraped_grp))
        except Exception as e:
            print(f'{error}{r} Failed to join source group: {e}')
            continue

        # Fetching only online members
        try:
            scraped_grp_entity = client.get_entity(scraped_grp)
            members = client.get_participants(scraped_grp_entity, aggressive=False)
            online_members = [
                m for m in members
                if isinstance(m.status, UserStatusOnline)  # Check if the user is online
            ]
        except Exception as e:
            print(f'{error}{r} Failed to fetch members: {e}')
            continue

        print(f'{info}{lg} Found {w}{len(online_members)}{lg} online members.')

        # Joining the target group
        try:
            if '/joinchat/' in target_grp:
                invite_hash = target_grp.split('/joinchat/')[1]
                client(ImportChatInviteRequest(invite_hash))
            else:
                client(JoinChannelRequest(target_grp))
            target_entity = client.get_entity(target_grp)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        except Exception as e:
            print(f'{error}{r} Failed to join target group: {e}')
            continue

        # Adding online members to target group
        for user in online_members:
            if user.bot:
                continue
            try:
                client(InviteToChannelRequest(target_details, [user]))
                print(f'{success}{lg} Added member: {w}{user.username or user.id}')
                time.sleep(sleep_time)
            except Exception as e:
                print(f'{error}{r} Failed to add member: {e}')
                continue

        client.disconnect()
        print(f'{info}{lg} Finished processing account: {acc[0]}')

    print(f'{success}{lg} All online members added successfully!{rs}')

# Fetch groups Online Members

def fetch_and_add_online_members():
    def banner():
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
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # Initialization and user input
    accounts = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')

    groups = {}
    for acc in accounts:
        client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        client.connect()
        client.start(acc[0])
        print(f'{info}{lg} Logged in as {client.get_me().first_name}')

        try:
            dialogs = client.get_dialogs()
            for dialog in dialogs:
                if dialog.is_group or dialog.is_channel:
                    entity = dialog.entity
                    if hasattr(entity, 'access_hash'):
                        groups[f"{entity.id}:{entity.access_hash}"] = dialog.name
        except Exception as e:
            print(f'{error}{r} Failed to fetch groups for {acc[0]}: {e}')
            client.disconnect()
            continue

        client.disconnect()

    if not groups:
        print(f'{error}{r} No groups found for any account.')
        return

    print(f'\n{info}{lg} Available Groups:')
    for i, (grp_key, grp_name) in enumerate(groups.items(), start=1):
        print(f'{i}. {grp_name}')
    
    selected_group_idx = int(input(f'\n{INPUT}{cy} Select the group to scrape online members from (Enter number): {r}'))
    selected_group_key = list(groups.keys())[selected_group_idx - 1]
    selected_group_id, selected_group_hash = map(int, selected_group_key.split(':'))

    target_grp = input(f'{INPUT}{cy} Enter group URL to add members: {r}')
    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request: {r}'))

    for acc in accounts:
        client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        client.connect()
        client.start(acc[0])
        print(f'{info}{lg} Logged in as {client.get_me().first_name}')

        # Fetching only online members
        try:
            scraped_grp_entity = InputPeerChannel(selected_group_id, selected_group_hash)
            members = client.get_participants(scraped_grp_entity, aggressive=False)
            online_members = [
                m for m in members
                if isinstance(m.status, UserStatusOnline)  # Check if the user is online
            ]
        except Exception as e:
            print(f'{error}{r} Failed to fetch members: {e}')
            continue

        print(f'{info}{lg} Found {w}{len(online_members)}{lg} online members.')

        # Joining the target group
        try:
            if '/joinchat/' in target_grp:
                invite_hash = target_grp.split('/joinchat/')[1]
                client(ImportChatInviteRequest(invite_hash))
            else:
                client(JoinChannelRequest(target_grp))
            target_entity = client.get_entity(target_grp)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        except Exception as e:
            print(f'{error}{r} Failed to join target group: {e}')
            continue

        # Adding online members to target group
        for user in online_members:
            if user.bot:
                continue
            try:
                client(InviteToChannelRequest(target_details, [user]))
                print(f'{success}{lg} Added member: {w}{user.username or user.id}')
                time.sleep(sleep_time)
            except Exception as e:
                print(f'{error}{r} Failed to add member: {e}')
                continue

        client.disconnect()
        print(f'{info}{lg} Finished processing account: {acc[0]}')

    print(f'{success}{lg} All online members added successfully!{rs}')


# Self Joined Groups

def start_scraping_and_adding():
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
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            

    accounts = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

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
        time.sleep(0.5)
        clnt.disconnect()

    print(f'{info} Sessions created!')
    clr()
    banner()
    print('Adding Account To Scrapeleet Channels in case you wanna speak to us')
    auto_join_group()
    print('All Account added successfully to Scrapeleet group\n')

    print("Loading and Checking for verifications")
    time.sleep(5)
    auto_join_group_smmleet()

    def log_status(scraped, index):
        with open('status.dat', 'wb') as f:
            pickle.dump([scraped, int(index)], f)
        print(f'{info}{lg} Session stored in {w}status.dat{lg}')

    def exit_window():
        input(f'\n{cy} Press enter to exit...')
        clr()
        banner()
        sys.exit()

    accounts = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want Use In Adding: {r}'))
    to_use = accounts[:number_of_accs]

    for acc in to_use:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        c.connect()

        dialogs = c.get_dialogs()
        groups = [d for d in dialogs if d.is_group or d.is_channel]
        print(f'\n{lg}Available groups for {acc[0]}:')
        for i, group in enumerate(groups):
            print(f'{i + 1}. {group.title}')

        group_index = int(input(f'{INPUT}{cy} Select a group to scrape members from (1-{len(groups)}): {r}')) - 1
        scraped_grp = groups[group_index].id

        group_index_target = int(input(f'{INPUT}{cy} Select a group to add members to (1-{len(groups)}): {r}')) - 1
        target_grp = groups[group_index_target].id

        members = c.get_participants(scraped_grp, aggressive=False)
        print(f'{info}{lg} Scraping members from {groups[group_index].title}...')

        sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request{w}[{lg}0 for None{w}]: {r}'))
        
        for member in members:
            try:
                c(InviteToChannelRequest(target_grp, [member]))
                print(f'{success}{lg} Added member {cy}{member.username}')
                time.sleep(sleep_time)
            except Exception as e:
                print(f'{error}{r} Error: {e}')
                time.sleep(5)
                continue
        
        print(f'{info}{lg} Finished adding members to {groups[group_index_target].title}!{rs}')
        c.disconnect()


# Message Moving
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

def move_messages():
    def banner():
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
        print('Contact below address for premium script')
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    accounts = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

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

    scraped_grp = input(f'{INPUT}{cy} Public/Private group URL link to scrape messages: {r}')
    target = input(f'{INPUT}{cy} Enter group URL link to move messages to: {r}')
    message_limit = int(input(f'{INPUT}{cy} Enter the number of messages to copy: {r}'))
    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request [suggest 30]: {r}'))

    account_clients = []
    for acc in accounts:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        c.start(acc[0])
        account_clients.append((acc[0], c))

    # Connect to groups
    for _, client in account_clients:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            client(ImportChatInviteRequest(g_hash))
        else:
            client(JoinChannelRequest(scraped_grp))

        if '/joinchat/' in target:
            g_hash = target.split('/joinchat/')[1]
            client(ImportChatInviteRequest(g_hash))
        else:
            client(JoinChannelRequest(target))

    # Retrieve messages
    messages = account_clients[0][1].get_messages(scraped_grp, limit=message_limit)

    # Move messages
    account_index = 0
    for msg in messages:
        try:
            acc_phone, client = account_clients[account_index]
            target_details = client.get_entity(target)

            if msg.media:
                # Forward media messages
                client(ForwardMessagesRequest(
                    from_peer=scraped_grp,
                    id=[msg.id],
                    to_peer=target_details
                ))
                print(f'{success}{lg} User: {cy}{acc_phone}{lg} -- Moved media message: {cy}{msg.id}')
            else:
                # Send text messages
                client(SendMessageRequest(target_details, msg.text))
                print(f'{success}{lg} User: {cy}{acc_phone}{lg} -- Moved message: {cy}{msg.text}')

            if sleep_time > 0:
                time.sleep(sleep_time)

            account_index = (account_index + 1) % len(account_clients)

        except Exception as e:
            print(f'{error}{r} Error moving message: {e}')
            continue

    # Disconnect clients
    for _, client in account_clients:
        client.disconnect()

    print(f'{info}{lg} Finished moving messages!{rs}')


# def move_messages():
#     def banner():
#         b = [
#             '░█████╗░██████╗░██████╗░███████╗██████╗░',
#             '██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',
#             '███████║██║░░██║██║░░██║█████╗░░██████╔╝',
#             '██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗',
#             '██║░░██║██████╔╝██████╔╝███████╗██║░░██║',
#             '╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝'
#         ]
#         for char in b:
#             print(f'{random.choice(colors)}{char}{rs}')
#         print('Contact below address for get premium script')
#         print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
#         print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

#     def clr():
#         if os.name == 'nt':
#             os.system('cls')
#         else:
#             os.system('clear')

#     accounts = []
#     with open('vars.txt', 'rb') as f:
#         while True:
#             try:
#                 accounts.append(pickle.load(f))
#             except EOFError:
#                 break

#     print('\n' + info + lg + ' Checking for banned accounts...' + rs)
#     banned = []
#     for a in accounts:
#         phn = a[0]
#         print(f'{plus}{grey} Checking {lg}{phn}')
#         clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         clnt.connect()
#         if not clnt.is_user_authorized():
#             try:
#                 clnt.send_code_request(phn)
#                 print('OK')
#             except:
#                 print(f'{error} {w}{phn} {r}is banned!{rs}')
#                 banned.append(a)
#         time.sleep(0.5)
#         clnt.disconnect()

#     for z in banned:
#         accounts.remove(z)
#         print(info + lg + ' Banned account removed' + rs)

#     print(f'{info} Sessions created!')
#     clr()
#     banner()

#     try:
#         with open('status.dat', 'rb') as f:
#             status = pickle.load(f)
#             f.close()
#             lol = input(f'{INPUT}{cy} Resume moving messages from {w}{status[0]}{lg}? [y/n]: {r}')
#             if 'y' in lol:
#                 scraped_grp = status[0]
#                 index = int(status[1])
#             else:
#                 if os.name == 'nt':
#                     os.system('del status.dat')
#                 else:
#                     os.system('rm status.dat')
#                 scraped_grp = input(f'{INPUT}{cy} Public/Private group URL link to scrape messages: {r}')
#                 index = 0
#     except:
#         scraped_grp = input(f'{INPUT}{cy} Public/Private group URL link to scrape messages: {r}')
#         index = 0

#     print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
#     number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want to Use in Moving: {r}'))
#     print(f'{info}{cy} Choose an option{lg}')
#     print(f'{cy}[0]{lg} Move to public group')
#     print(f'{cy}[1]{lg} Move to private group')
#     choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

#     print("If a group has a security verification when joining, make sure you join the group yourself and complete the verification process.")
#     print("This will help you avoid being removed while moving messages on Telegram.")

#     print("The scraper can only join the group but cannot handle the verification questions and answers.")
#     print("Failure to verify the group may result in restrictions from Telegram.\n")

#     target = input(f'{INPUT}{cy} Enter group URL link to move messages to: {r}')
#     sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request {w}[{lg}0 for None, suggest 30{w}]: {r}'))

#     to_use = list(accounts[:number_of_accs])
#     for l in to_use: accounts.remove(l)
#     with open('vars.txt', 'wb') as f:
#         for a in accounts:
#             pickle.dump(a, f)
#         for ab in to_use:
#             pickle.dump(ab, f)

#     account_index = 0
#     account_clients = []
#     for acc in to_use:
#         c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         c.start(acc[0])
#         account_clients.append((acc[0], c))

#     # Connect to the scraped group and target group for each account
#     for _, client in account_clients:
#         if '/joinchat/' in scraped_grp:
#             g_hash = scraped_grp.split('/joinchat/')[1]
#             client(ImportChatInviteRequest(g_hash))
#         else:
#             client(JoinChannelRequest(scraped_grp))
        
#         if '/joinchat/' in target:
#             grp_hash = target.split('/joinchat/')[1]
#             client(ImportChatInviteRequest(grp_hash))
#         else:
#             client(JoinChannelRequest(target))

#     # Retrieving messages from the source group
#     try:
#         message_limit = int(input('Enter amount of messages to copy (e.g., 10): '))
#         messages = account_clients[0][1].get_messages(scraped_grp, limit=message_limit)
#     except Exception as e:
#         print(f'{error}{r} Couldn\'t retrieve messages')
#         print(f'{error}{r} {e}')
#         return

#     for msg in messages:
#         try:
#             acc_phone, client = account_clients[account_index]
#             target_details = client.get_entity(target)
#             client(SendMessageRequest(target_details, msg.text))
#             print(f'{success}{lg} User: {cy}{acc_phone}{lg} -- Moved message: {cy}{msg.text}')

#             if sleep_time > 0:
#                 time.sleep(sleep_time)
            
#             account_index = (account_index + 1) % len(account_clients)

#         except Exception as e:
#             print(f'{error}{r} Error moving message: {e}')
#             continue

#     for _, client in account_clients:
#         client.disconnect()

#     print(f'{info}{lg} Finished moving messages!{rs}')

def move_old_messages():
    def banner():
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
        print('Contact below address for premium script')
        print(f'{lg}Version: {w}2.1{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    accounts = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

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

    scraped_grp = input(f'{INPUT}{cy} Public/Private group URL link to scrape messages: {r}')
    target = input(f'{INPUT}{cy} Enter group URL link to move messages to: {r}')
    message_limit = int(input(f'{INPUT}{cy} Enter the number of messages to copy: {r}'))
    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request [suggest 30]: {r}'))

    account_clients = []
    for acc in accounts:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        c.start(acc[0])
        account_clients.append((acc[0], c))

    # Connect to groups
    for _, client in account_clients:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            client(ImportChatInviteRequest(g_hash))
        else:
            client(JoinChannelRequest(scraped_grp))

        if '/joinchat/' in target:
            g_hash = target.split('/joinchat/')[1]
            client(ImportChatInviteRequest(g_hash))
        else:
            client(JoinChannelRequest(target))

    # Retrieve older messages
    messages = []
    total_messages = account_clients[0][1].get_messages(scraped_grp, limit=0).total
    offset_id = total_messages

    while len(messages) < message_limit and offset_id > 0:
        batch = account_clients[0][1].get_messages(scraped_grp, limit=min(message_limit - len(messages), 100), offset_id=offset_id)
        if not batch:
            break
        messages.extend(batch)
        offset_id = batch[-1].id

    messages.reverse()  # Start from the oldest message

    # Move messages
    account_index = 0
    for msg in messages:
        try:
            acc_phone, client = account_clients[account_index]
            target_details = client.get_entity(target)

            if msg.media:
                # Forward media messages
                client(ForwardMessagesRequest(
                    from_peer=scraped_grp,
                    id=[msg.id],
                    to_peer=target_details
                ))
                print(f'{success}{lg} User: {cy}{acc_phone}{lg} -- Moved media message: {cy}{msg.id}')
            else:
                # Send text messages
                client(SendMessageRequest(target_details, msg.text))
                print(f'{success}{lg} User: {cy}{acc_phone}{lg} -- Moved message: {cy}{msg.text}')

            if sleep_time > 0:
                time.sleep(sleep_time)

            account_index = (account_index + 1) % len(account_clients)

        except Exception as e:
            print(f'{error}{r} Error moving message: {e}')
            continue

    # Disconnect clients
    for _, client in account_clients:
        client.disconnect()

    print(f'{info}{lg} Finished moving old messages!{rs}')



# Move Message From Groups That does not have a shared link

def transfer_group_messages():
    def banner():
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
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    accounts = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

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
    print('Adding Account To Scrapeleet Channels in case you wanna speak to us')
    auto_join_group()
    print('All Account added successfully to Scrapeleet group\n')

    print("Loading and Checking for verifications")
    time.sleep(5)
    auto_join_group_smmleet()

    # Fetching all groups from the account
    all_groups = []
    for a in accounts:
        phn = a[0]
        print(f'{plus}{grey} Fetching groups for {lg}{phn}')
        clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        clnt.connect()
        if clnt.is_user_authorized():
            dialogs = clnt.get_dialogs()
            groups = [d for d in dialogs if d.is_group]
            all_groups.extend(groups)
        clnt.disconnect()

    if not all_groups:
        print(f'{error} No groups found.')
        return

    # Allow the user to select a group to scrape messages from
    print(f'{info}{lg} Available groups to scrape messages from:')
    for idx, group in enumerate(all_groups, 1):
        print(f'{cy}[{idx}]{lg} {group.name}')

    selected_group_idx = int(input(f'{INPUT}{cy} Select the group number to scrape messages from: {r}')) - 1
    if selected_group_idx < 0 or selected_group_idx >= len(all_groups):
        print(f'{error}{r} Invalid group selection!{rs}')
        return

    # Get the group's link (username or ID)
    group = all_groups[selected_group_idx]
    if hasattr(group.entity, 'username'):
        scraped_grp = f"https://t.me/{group.entity.username}"
    else:
        scraped_grp = f"https://t.me/c/{group.entity.id}"

    print(f'{info}{lg} Selected group to scrape messages from: {w}{scraped_grp}{rs}')

    try:
        with open('status.dat', 'rb') as f:
            status = pickle.load(f)
            f.close()
            lol = input(f'{INPUT}{cy} Resume moving messages from {w}{status[0]}{lg}? [y/n]: {r}')
            if 'y' in lol:
                index = int(status[1])
            else:
                if os.name == 'nt':
                    os.system('del status.dat')
                else:
                    os.system('rm status.dat')
                index = 0
    except:
        index = 0

    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want to Use in Moving: {r}'))
    print(f'{info}{cy} Choose an option{lg}')
    print(f'{cy}[0]{lg} Move to public group')
    print(f'{cy}[1]{lg} Move to private group')
    choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

    target = input(f'{INPUT}{cy} Enter group URL link to move messages to: {r}')
    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request {w}[{lg}0 for None, suggest 30{w}]: {r}'))

    to_use = list(accounts[:number_of_accs])
    for l in to_use: accounts.remove(l)
    with open('vars.txt', 'wb') as f:
        for a in accounts:
            pickle.dump(a, f)
        for ab in to_use:
            pickle.dump(ab, f)

    account_index = 0
    account_clients = []
    for acc in to_use:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        c.start(acc[0])
        account_clients.append((acc[0], c))

    # Connect to the scraped group and target group for each account
    for _, client in account_clients:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            client(ImportChatInviteRequest(g_hash))
        else:
            client(JoinChannelRequest(scraped_grp))
        
        if '/joinchat/' in target:
            grp_hash = target.split('/joinchat/')[1]
            client(ImportChatInviteRequest(grp_hash))
        else:
            client(JoinChannelRequest(target))

    # Retrieving messages from the source group
    try:
        message_limit = int(input('Enter amount of messages to copy (e.g., 10): '))
        messages = account_clients[0][1].get_messages(scraped_grp, limit=message_limit)
    except Exception as e:
        print(f'{error}{r} Couldn\'t retrieve messages')
        print(f'{error}{r} {e}')
        return

    for msg in messages:
        try:
            acc_phone, client = account_clients[account_index]
            target_details = client.get_entity(target)
            client(SendMessageRequest(target_details, msg.text))
            print(f'{success}{lg} User: {cy}{acc_phone}{lg} -- Moved message: {cy}{msg.text}')

            if sleep_time > 0:
                time.sleep(sleep_time)
            
            account_index = (account_index + 1) % len(account_clients)

        except Exception as e:
            print(f'{error}{r} Error moving message: {e}')
            continue

    for _, client in account_clients:
        client.disconnect()

    print(f'{info}{lg} Finished moving messages!{rs}')




# Hidden Groups Members Adder

# def hidden_members():
#     def banner():
#         # fancy logo
#         b = [
#             '░█████╗░██████╗░██████╗░███████╗██████╗░',
#             '██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',
#             '███████║██║░░██║██║░░██║█████╗░░██████╔╝',
#             '██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗',
#             '██║░░██║██████╔╝██████╔╝███████╗██║░░██║',
#             '╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝'
#         ]
#         for char in b:
#             print(f'{random.choice(colors)}{char}{rs}')
#         print('Contact below address for get premium script')
#         print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
#         print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

#     # function to clear screen
#     def clr():
#         if os.name == 'nt':
#             os.system('cls')
#         else:
#             os.system('clear')

#     accounts = []
#     f = open('vars.txt', 'rb')
#     while True:
#         try:
#             accounts.append(pickle.load(f))
#         except EOFError:
#             break

#     # create sessions(if any) and check for any banned accounts
#     # TODO: Remove code input(just to check if an account is banned)
#     print('\n' + info + lg + ' Checking for banned accounts...' + rs)
#     for a in accounts:
#         phn = a[0]
#         print(f'{plus}{grey} Checking {lg}{phn}')
#         clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         clnt.connect()
#         banned = []
#         if not clnt.is_user_authorized():
#             try:
#                 clnt.send_code_request(phn)
#                 print('OK')
#             except PhoneNumberBannedError:
#                 print(f'{error} {w}{phn} {r}is banned!{rs}')
#                 banned.append(a)
#         for z in banned:
#             accounts.remove(z)
#             print(info + lg + ' Banned account removed[Remove permanently using manager.py]' + rs)
#         time.sleep(0.5)
#         clnt.disconnect()

#     print(f'{info} Sessions created!')
#     clr()
#     banner()

#     # func to log scraping details(link of the grp to scrape and current index) in order to resume later
#     def log_status(scraped, index):
#         with open('status.dat', 'wb') as f:
#             pickle.dump([scraped, int(index)], f)
#             f.close()
#         print(f'{info}{lg} Session stored in {w}status.dat{lg}')

#     def exit_window():
#         input(f'\n{cy} Press enter to exit...')
#         clr()
#         banner()
#         sys.exit()

#     # read user details
#     try:
#         # request to resume adding
#         with open('status.dat', 'rb') as f:
#             status = pickle.load(f)
#             f.close()
#             lol = input(f'{INPUT}{cy} Resume scraping hidden members from {w}{status[0]}{lg}? [y/n]: {r}')
#             if 'y' in lol:
#                 scraped_grp = status[0]
#                 index = int(status[1])
#             else:
#                 if os.name == 'nt':
#                     os.system('del status.dat')
#                 else:
#                     os.system('rm status.dat')
#                 scraped_grp = input(f'{INPUT}{cy} Public/Private group url link to scrape members: {r}')
#                 index = 0
#     except:
#         scraped_grp = input(f'{INPUT}{cy} Public/Private group url link to scrape hidden members: {r}')
#         index = 0

#     # load all the accounts(phonenumbers)
#     accounts = []
#     f = open('vars.txt', 'rb')
#     while True:
#         try:
#             accounts.append(pickle.load(f))
#         except EOFError:
#             break

#     print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
#     number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want Use In Adding: {r}'))
#     print(f'{info}{cy} Choose an option{lg}')
#     print(f'{cy}[0]{lg} Add to public group')
#     print(f'{cy}[1]{lg} Add to private group')
#     choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

#     if choice == 0:
#         target = str(input(f'{INPUT}{cy} Enter public group url link: {r}'))
#     else:
#         target = str(input(f'{INPUT}{cy} Enter private group url link: {r}'))

#     print(f'{grey}_' * 50)
#     status_choice = str(input(f'{INPUT}{cy} Do you wanna add active hidden members?[y/n]: {r}'))
#     to_use = list(accounts[:number_of_accs])
#     for l in to_use: accounts.remove(l)
#     with open('vars.txt', 'wb') as f:
#         for a in accounts:
#             pickle.dump(a, f)
#         for ab in to_use:
#             pickle.dump(ab, f)
#         f.close()

#     sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request{w}[{lg}0 for None, I suggest entering 30 to add hidden members properly{w}]: {r}'))
#     print(f'{info}{lg} Joining group from {w}{number_of_accs} accounts...')
#     print(f'{grey}-' * 50)
#     print(f'{success}{lg} -- Adding hidden members from {w}{len(to_use)}{lg} account(s) --')
#     adding_status = 0
#     approx_members_count = 0

#     for acc in to_use:
#         stop = index + 60
#         c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
#         c.start(acc[0])
#         acc_name = c.get_me().first_name
#         try:
#             if '/joinchat/' in scraped_grp:
#                 g_hash = scraped_grp.split('/joinchat/')[1]
#                 try:
#                     c(ImportChatInviteRequest(g_hash))
#                     print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
#                 except UserAlreadyParticipantError:
#                     pass
#             else:
#                 c(JoinChannelRequest(scraped_grp))
#                 print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
#             scraped_grp_entity = c.get_entity(scraped_grp)
#             if choice == 0:
#                 c(JoinChannelRequest(target))
#                 print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to add')
#                 target_entity = c.get_entity(target)
#                 target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
#             else:
#                 try:
#                     grp_hash = target.split('/joinchat/')[1]
#                     c(ImportChatInviteRequest(grp_hash))
#                     print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to add')
#                 except UserAlreadyParticipantError:
#                     pass
#                 target_entity = c.get_entity(target)
#                 target_details = target_entity
#         except Exception as e:
#             print(f'{error}{r} User: {cy}{acc_name}{lg} -- Failed to join group')
#             print(f'{error} {r}{e}')
#             continue
#         print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Retrieving entities...')
#         c.get_dialogs()
#         try:
#             members = []
#             members = c.get_participants(scraped_grp_entity, aggressive=False)
#         except Exception as e:
#             print(f'{error}{r} Couldn\'t scrape members')
#             print(f'{error}{r} {e}')
#             continue
#         approx_members_count = len(members)
#         assert approx_members_count != 0
#         if index >= approx_members_count:
#             print(f'{error}{lg} No members to add!')
#             continue
#         print(f'{info}{lg} Start: {w}{index}')
#         adding_status = 0
#         peer_flood_status = 0
#         for user in members[index:stop]:
#             index += 1
#             if user.bot:
#                 continue
#             try:
#                 c(InviteToChannelRequest(target_details, [user]))
#                 print(f'{success}{lg} User: {cy}{acc_name}{lg} -- Added member {cy}{user.username}')
#                 time.sleep(sleep_time)
#                 adding_status += 1
#             except UserAlreadyParticipantError:
#                 print(f'{info}{cy} User: {cy}{acc_name}{lg} -- User {cy}{user.username} already added!{rs}')
#             except UserPrivacyRestrictedError:
#                 print(f'{info}{cy} User: {cy}{acc_name}{lg} -- User {cy}{user.username} has privacy restrictions!{rs}')
#             except ChatWriteForbiddenError:
#                 print(f'{info}{cy} User: {cy}{acc_name}{lg} -- No permission to write in the group!{rs}')
#             except PeerFloodError:
#                 peer_flood_status += 1
#                 print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Peer flood error...{rs}')
#                 if peer_flood_status == 5:
#                     print(f'{info}{lg} You have been rate-limited, waiting for 60 seconds...{rs}')
#                     time.sleep(60)
#                     continue
#             except ChatAdminRequiredError:
#                 print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Admin permission required to add members!{rs}')
#             except FloodWaitError:
#                 print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Flood wait error! Sleeping for 15 seconds...{rs}')
#                 time.sleep(15)
#             except Exception as e:
#                 print(f'{error}{r} Error: {e}')
#                 continue
#             if stop == approx_members_count or index >= approx_members_count:
#                 break
#         if adding_status > 0:
#             log_status(scraped_grp, index)
#             print(f'{info}{lg} Successfully added {w}{adding_status} hidden members{lg} from account {w}{acc_name}')
#         c.disconnect()
#         print(f'{grey}-' * 50)

#     print(f'{info}{lg} Finished adding members!{rs}')

def hidden_members():
    def banner():
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
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

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

    try:
        scraped_grp = input(f'{INPUT}{cy} Public/Private group URL to scrape members: {r}')
    except:
        print(f'{error} Failed to input group link!')
        return

    scrape_limit = int(input(f'{INPUT}{cy} Enter number of members to scrape per account (limit: 50): {r}'))

    number_of_accs = int(input(f'{INPUT}{cy} How many accounts do you want to use for adding? {r}'))
    print(f'{info}{cy} Choose an option{lg}')
    print(f'{cy}[0]{lg} Add to public group')
    print(f'{cy}[1]{lg} Add to private group')
    choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

    if choice == 0:
        target = str(input(f'{INPUT}{cy} Enter public group URL link: {r}'))
    else:
        target = str(input(f'{INPUT}{cy} Enter private group URL link: {r}'))

    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request [suggest 30]: {r}'))

    print(f'{info}{lg} Joining the destination group from {w}{number_of_accs} accounts...')

    for acc in accounts[:number_of_accs]:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session...')
        c.start(acc[0])

        # Step 1: Join the destination group
        try:
            if choice == 0:
                target_entity = c.get_entity(target)
            else:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                target_entity = c.get_entity(target)

            print(f'{success}{lg} User {cy}{acc[0]} joined the group successfully!{rs}')
        except UserAlreadyParticipantError:
            print(f'{info}{cy} User {acc[0]} is already a member of the destination group!{rs}')
        except Exception as e:
            print(f'{error}{r} User {acc[0]} failed to join the group. Error: {e}{rs}')
            c.disconnect()
            continue  # Skip to the next account if joining fails

        # Step 2: Scrape members from the source group
        try:
            scraped_grp_entity = c.get_entity(scraped_grp)
            active_members = []
            for message in c.iter_messages(scraped_grp_entity):
                if len(active_members) >= scrape_limit:
                    break
                if message.sender_id:
                    try:
                        user = c.get_entity(message.sender_id)
                        if user not in active_members:
                            active_members.append(user)
                    except Exception as e:
                        print(f'{error}{r} Could not fetch user {message.sender_id}. Error: {e}')
                        continue

            print(f'{info}{lg} Retrieved {len(active_members)} active members!')

            # Step 3: Add members to the destination group
            for user in active_members:
                try:
                    c(InviteToChannelRequest(target_entity, [user]))
                    print(f'{success}{lg} Added member {cy}{user.username}')
                    time.sleep(sleep_time)
                except UserAlreadyParticipantError:
                    print(f'{info}{cy} User {cy}{user.username} already added!{rs}')
                except UserPrivacyRestrictedError:
                    print(f'{info}{cy} User {cy}{user.username} has privacy restrictions!{rs}')
                except Exception as e:
                    print(f'{error}{r} Failed to add user. Error: {e}')
        except Exception as e:
            print(f'{error}{r} Could not process group. Error: {e}')
        finally:
            c.disconnect()
            print(f'{grey}-' * 50)

    print(f'{info}{lg} Finished adding active members!{rs}')




def scrape_hidden_members_from_groups():
    def banner():
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
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

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
    print('Adding Account To Scrapeleet Channels in case you wanna speak to us')
    auto_join_group()
    print('All Account added successfully to Scrapeleet group\n')

    print("Loading and Checking for verifications")
    time.sleep(5)
    auto_join_group_smmleet()

    # Fetch all groups from all accounts
    group_dict = {}
    for acc in accounts:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        c.start(acc[0])
        try:
            groups = [dialog.entity for dialog in c.iter_dialogs() if getattr(dialog.entity, 'megagroup', False)]
            for group in groups:
                group_dict[group.title] = group
            print(f'{success}{lg} Fetched groups from {cy}{acc[0]}{rs}')
        except Exception as e:
            print(f'{error}{r} Failed to fetch groups for {acc[0]}. Error: {e}')
        finally:
            c.disconnect()

    if not group_dict:
        print(f'{error}{r} No groups found! Exiting...')
        return

    # Display fetched groups to the user
    print(f'{info}{lg} Available Groups:')
    for idx, group_name in enumerate(group_dict.keys()):
        print(f'{idx + 1}. {group_name}')

    try:
        selected_idx = int(input(f'{INPUT}{cy} Select a group to scrape members from (1-{len(group_dict)}): {r}')) - 1
        selected_group = list(group_dict.values())[selected_idx]
    except:
        print(f'{error} Invalid selection! Exiting...')
        return

    scrape_limit = int(input(f'{INPUT}{cy} Enter number of members to scrape per each account (limit: 50): {r}'))

    accounts = []
    f = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(f))
        except EOFError:
            break

    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want Use In Adding: {r}'))
    print(f'{info}{cy} Choose an option{lg} ')
    print(f'{cy}[0]{lg} Add to public group')
    print(f'{cy}[1]{lg} Add to private group')
    choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

    if choice == 0:
        target = str(input(f'{INPUT}{cy} Enter public group url link: {r}'))
    else:
        target = str(input(f'{INPUT}{cy} Enter private group url link: {r}'))

    sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request{w}[{lg}0 for None, suggest 30]: {r}'))
    print(f'{info}{lg} Joining group from {w}{number_of_accs} accounts...')
    print(f'{grey}-' * 50)

    for acc in accounts[:number_of_accs]:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session...')
        c.start(acc[0])

        try:
            active_members = []
            for message in c.iter_messages(selected_group):
                if len(active_members) >= scrape_limit:
                    break
                if message.sender_id:
                    try:
                        user = c.get_entity(message.sender_id)
                        if user not in active_members:
                            active_members.append(user)
                    except Exception as e:
                        print(f'{error}{r} Could not fetch user {message.sender_id}. Error: {e}')
                        continue

            print(f'{info}{lg} Retrieved {len(active_members)} active members!')

            if choice == 0:
                target_entity = c.get_entity(target)
                target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
            else:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                target_entity = c.get_entity(target)
                target_details = target_entity

            for user in active_members:
                try:
                    c(InviteToChannelRequest(target_details, [user]))
                    print(f'{success}{lg} Added member {cy}{user.username}')
                    time.sleep(sleep_time)
                except UserAlreadyParticipantError:
                    print(f'{info}{cy} User {cy}{user.username} already added!{rs}')
                except UserPrivacyRestrictedError:
                    print(f'{info}{cy} User {cy}{user.username} has privacy restrictions!{rs}')
                except Exception as e:
                    print(f'{error}{r} Failed to add user. Error: {e}')
        except Exception as e:
            print(f'{error}{r} Could not process group. Error: {e}')
        finally:
            c.disconnect()
            print(f'{grey}-' * 50)

    print(f'{info}{lg} Finished adding active members!{rs}')






# Send Bulks Message to all scraped members

def scrape_and_send_bulk_message():
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
        print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
        print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

    # function to clear screen
    def clr():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # Load accounts from saved sessions
    accounts = []
    f = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(f))
        except EOFError:
            break

    # Check for banned accounts and remove them
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
            except PhoneNumberBannedError:
                print(f'{error} {w}{phn} {r}is banned!{rs}')
                banned.append(a)
        for z in banned:
            accounts.remove(z)
            print(info + lg + ' Banned account removed[Remove permanently using manager.py]' + rs)
        time.sleep(0.5)
        clnt.disconnect()

    # Function to log scraping status
    def log_status(scraped, index):
        with open('status.dat', 'wb') as f:
            pickle.dump([scraped, int(index)], f)

    # Prompt user for scraping group URL and other details
    scraped_grp = input(f'{INPUT}{cy} Public/Private group URL to scrape members: {r}')
    index = 0
    print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    number_of_accs = int(input(f'{INPUT}{cy} How Many Accounts You Want to Use for Scraping: {r}'))
    to_use = list(accounts[:number_of_accs])

    # Get the number of members to send messages to
    target_members = int(input(f'{INPUT}{cy} Enter the number of members to send messages to: {r}'))

    # Get the number of messages to send per account
    messages_per_account = int(input(f'{INPUT}{cy} Enter the number of messages to send per account: {r}'))

    # Send bulk message to scraped members
    message_to_send = input(f'{INPUT}{cy} Enter the message to send to scraped members: {r}')
    delay_time = int(input(f'{INPUT}{cy} Enter delay time (in seconds) between messages to avoid flood error: {r}'))

    print(f'{info}{lg} Scraping members from {w}{scraped_grp}{lg}...')
    adding_status = 0
    approx_members_count = 0

    for acc in to_use:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- Starting session... ')
        c.start(acc[0])
        acc_name = c.get_me().first_name
        try:
            if '/joinchat/' in scraped_grp:
                g_hash = scraped_grp.split('/joinchat/')[1]
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
            else:
                c(JoinChannelRequest(scraped_grp))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined group to scrape')
            scraped_grp_entity = c.get_entity(scraped_grp)
        except Exception as e:
            print(f'{error}{r} User: {cy}{acc_name}{lg} -- Failed to join group')
            print(f'{error} {r}{e}')
            continue

        print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Retrieving members...')
        try:
            members = c.get_participants(scraped_grp_entity, aggressive=False)
        except Exception as e:
            print(f'{error}{r} Couldn\'t scrape members')
            print(f'{error}{r} {e}')
            continue
        approx_members_count = len(members)

        if index >= approx_members_count:
            print(f'{error}{lg} No members to scrape! Exiting...{rs}')
            continue
        print(f'{info}{lg} Scraping members starting from {w}{index}{lg}...')

        message_count = 0  # Track messages sent for this account

        for user in members[index:]:
            if adding_status >= target_members:
                break  # Stop sending if target number of messages is reached
            index += 1
            if user.bot:
                continue
            try:
                # Send bulk message
                c.send_message(user.id, message_to_send)
                print(f'{success}{lg} User: {cy}{acc_name}{lg} -- Sent message to {cy}{user.username}')
                time.sleep(delay_time)
                adding_status += 1
                message_count += 1

                # If the account has sent the specified number of messages, move to the next account
                if message_count >= messages_per_account:
                    print(f'{info}{lg} {w}{acc_name}{lg} -- Sent {message_count} messages, moving to next account.')
                    break

            except UserPrivacyRestrictedError:
                print(f'{info}{cy} User: {cy}{acc_name}{lg} -- User {cy}{user.username} has privacy restrictions!{rs}')
            except PeerFloodError:
                print(f'{error}{cy} User: {cy}{acc_name}{lg} -- Peer flood error, waiting for 60 seconds...{rs}')
                time.sleep(60)
                continue
            except Exception as e:
                print(f'{error}{r} Error: {e}')
                time.sleep(5)
                continue

        if adding_status >= target_members:
            break  # Stop sending if target number of messages is reached

        if adding_status > 0:
            log_status(scraped_grp, index)
            print(f'{info}{lg} Successfully sent {w}{adding_status}{lg} messages from account {w}{acc_name}')
        c.disconnect()

    print(f'{info}{lg} Finished sending bulk messages!{rs}')



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


# Only 3 Devices

import os
import uuid
import platform

# File to store the unique device identifiers
DEVICE_FILE = "device_ids.txt"
MAX_DEVICES = 3

def get_device_id():
    """
    Get a unique identifier for the device.
    This example uses the MAC address, but you could use other unique identifiers like UUID.
    """
    if platform.system() == "Linux" or platform.system() == "Darwin":
        # Get MAC address for Linux and macOS
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 8*6, 8)][::-1])
        return mac
    elif platform.system() == "Windows":
        # Get a unique machine ID on Windows
        return str(uuid.getnode())  # MAC address or fallback to another unique ID
    return str(uuid.getnode())  # Fallback to UUID if OS is unsupported

def read_device_ids():
    """
    Read the stored device IDs from the device file.
    """
    if os.path.exists(DEVICE_FILE):
        with open(DEVICE_FILE, "r") as file:
            return file.read().splitlines()
    return []

def save_device_id(device_id):
    """
    Save the new device ID to the file.
    """
    with open(DEVICE_FILE, "a") as file:
        file.write(device_id + "\n")

def is_device_allowed():
    """
    Check if the device is allowed to run the script (i.e., not exceeding the device limit).
    """
    device_id = get_device_id()
    device_ids = read_device_ids()

    if len(device_ids) >= MAX_DEVICES:
        print(f"Device limit reached ({MAX_DEVICES}). Cannot run the script on more devices.")
        return False
    
    # If device is not already in the list, add it
    if device_id not in device_ids:
        save_device_id(device_id)
        print(f"Device {device_id} registered successfully.")

    return True

def main_three_devices():
    if not is_device_allowed():
        print("Exiting... This device is not allowed to run the script.")
        return
    
    print("Script is running...")





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

    # Prompt for a valid token if none exists or if the token is invalid
    while True:
        if token is None:
            token = input(lg + "[+] Enter your purchase token or get it from https://scrapeleet.com: ")
        else:
            is_valid, user_id = verify_token(token)
            if is_valid:
                print(lg + f"[+] Loaded token verified for user ID: {user_id}. Access granted to the scraper.")
                save_token(token)
                break  
            else:
                print(r + "[!] Invalid or expired token. Please enter a valid token or purchase one from https://scrapeleet.com.")
                token = input(lg + "[+] Enter your purchase token: ")
                save_token(token)
                break 

    main_three_devices()

    """Display the main menu with options."""
    menu = f"""
{cy}╔════════════════════════════════════╗
{cy}║          {lg}Main Menu{cy}           ║
{cy}╚════════════════════════════════════╝
{lg}1.{rs} Manage Account
{lg}2.{rs} Automate Scraping and Members Adding
{lg}3.{rs} Automate Scraping and Online Members Adding 
{lg}4.{rs} Automate Scraping and Online Members Adding That has no share link 
{lg}5.{rs} Automate Scraping and Hidden Members Adding
{lg}6.{rs} Automate Scraping and Hidden Members Adding with No Share Links
{lg}7.{rs} Moving New Messages From Group to Group 
{lg}8.{rs} Send Bulk Messages to All Scraped Members (DMs)
{lg}9.{rs} Scrape and Add Members That has no Share Links
{lg}10.{rs} Moving New Messages From Group to Group That has no Share Links 
{lg}11.{rs} Move Old Messages From Group to Group
{lg}12.{rs} Exit Scrapeleet
"""

    while True:
        print(menu)
        choice = input(f'\n{INPUT}{cy} Select an action: {rs}')

        if choice == '1':
            manager()
        elif choice == '2':
            while True:
                automation()
        elif choice == '3':
            automation_online_only()
        elif choice == '4':
            fetch_and_add_online_members()
        elif choice == '5':
            hidden_members()
        elif choice == '6':
            scrape_hidden_members_from_groups()
        elif choice == '7':
            move_messages()
        elif choice == '8':
            scrape_and_send_bulk_message()
        elif choice == '9':
            start_scraping_and_adding()
        elif choice == '10':
            transfer_group_messages()
        elif choice == '11':
            move_old_messages()
        elif choice == '12':
            print('Thanks for using Scrapeleet!')
            break
        else:
            print(f'{error} {r}Invalid choice! Please select a valid option.{rs}')
            continue


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f'\n{error} {r}Operation interrupted by the user. Exiting...{rs}')
