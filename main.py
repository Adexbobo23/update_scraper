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
        print(f'{lg}[6] Check and remove restricted account')
        print(f'{lg}[7] Back to menu{n}')
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
                            break
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
                                break
                            except Exception as e:
                                if 'code' in str(e).lower():
                                    print(f'{error} Incorrect code entered. Please try again for {number}.')
                                else:
                                    print(f'{error} An error occurred: {e}')
                                    break
                    except Exception as e:
                        print(f'{error} Unable to login with {number}. Error: {e}')
                    finally:
                        c.disconnect()
                input(f'\nPress enter to go to the main menu...')
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
                    client = TelegramClient(f'sessions/{phone}', 3910389, '86f861352f0ab76a251866059a6adbd6')
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
                    print(f'{lg}[i] All banned accounts removed{n}')
                input('\nPress enter to go to the main menu...')

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
                input(f'\nPress enter to go to the main menu...')

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
                        file_url = 'https://raw.githubusercontent.com/Adexbobo23/scrapeleet_update/main/main.pyc'
                        response = requests.get(file_url)
                        response.raise_for_status()  # Check for HTTP request errors

                        # Backup existing file (overwrite if the backup already exists)
                        if os.path.exists('main.pyc'):
                            os.replace('main.pyc', 'main.pyc.bak')

                        # Save the updated file with UTF-8 encoding
                        with open('main.pyc', 'w', encoding='utf-8') as f:
                            f.write(response.text)
                        
                        print(f'{lg}[+] Successfully updated main.pyc to version {version}.')
                        input('Press enter to exit...')
                        exit()
                    except Exception as e:
                        print(f'{r}[!] Failed to update main.pyc. Error: {e}')
                        # Restore backup if update fails
                        if os.path.exists('main.pyc.bak'):
                            os.replace('main.pyc.bak', 'main.pyc')
                        print(f'{r}[!] Reverted to the previous version of main.pyc.')
                        input('Press enter to go to the main menu...')
                else:
                    print(f'{lg}[!] Update aborted.')
                    input('Press enter to go to the main menu...')
            else:
                print(f'{lg}[i] Your Telegram-Members-Adder is already up to date.')
                input('Press enter to go to the main menu...')


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
            input('\nPress enter to go to the main menu...')

        elif a == 6:
            print(f'\n{lg}[i] Checking for restricted accounts...')
            accounts = []
            restricted_accs = []
            with open('vars.txt', 'rb') as file:
                while True:
                    try:
                        accounts.append(pickle.load(file))
                    except EOFError:
                        break
            if not accounts:
                print(f'{r}[!] No accounts found. Please add some accounts first.')
                sleep(3)
            else:
                for account in accounts:
                    phone = str(account[0])
                    client = TelegramClient(f'sessions/{phone}', 3910389, '86f861352f0ab76a251866059a6adbd6')
                    client.connect()
                    try:
                        if not client.is_user_authorized():
                            client.send_code_request(phone)
                            restricted_accs.append(account)
                        else:
                            print(f'{lg}[+] {phone} is not restricted.')
                    except Exception as e:
                        print(f'{error} Error checking account {phone}: {e}')
                    finally:
                        client.disconnect()
                if restricted_accs:
                    print(f'{lg}Removing restricted accounts...')
                    for m in restricted_accs:
                        accounts.remove(m)
                    with open('vars.txt', 'wb') as f:
                        for acc in accounts:
                            pickle.dump(acc, f)
                    print(f'{lg}[+] Restricted accounts removed.')
                else:
                    print(f'{lg}No restricted accounts found.')
                input('\nPress enter to go to the main menu...')

        elif a == 7:
            clr()
            banner()
            break
            # sys.exit()
        else:
            print(f'{error} Invalid choice, please try again.')
            input('\nPress enter to go back to the main menu...')


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



def group_joiner():
    def banner():
        b = [
            '\033[92m░█████╗░██████╗░██████╗░███████╗██████╗░\033[0m',
            '\033[92m██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗\033[0m',
            '\033[92m███████║██║░░██║██║░░██║█████╗░░██████╔╝\033[0m',
            '\033[92m██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗\033[0m',
            '\033[92m██║░░██║██████╔╝██████╔╝███████╗██║░░██║\033[0m',
            '\033[92m╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝\033[0m'
        ]
        for char in b:
            print(char)
        print('\033[93mContact below address for get premium script\033[0m')
        print('\033[93mVersion: 2.0 | GitHub: @Scrapeleet\033[0m')
        print('\033[93mTelegram: @Scrapeleet | Instagram: @Scrapeleet\n\033[0m')

    def load_accounts():
        accounts = []
        with open('vars.txt', 'rb') as f:
            while True:
                try:
                    accounts.append(pickle.load(f))
                except EOFError:
                    break
        return accounts

    group_link = input("\033[96mEnter the group link you want the accounts to join: \033[0m")
    accounts = load_accounts()
    print(f'\033[94mTotal accounts: {len(accounts)}\033[0m')

    print("\033[96mChoose an option:\033[0m")
    print("\033[96m1. Join with one account\033[0m")
    print("\033[96m2. Join with all accounts\033[0m")
    choice = input("\033[96mEnter your choice (1/2): \033[0m")

    if choice == "1":
        phone = accounts[0][0]
        print(f"\033[92mJoining the group with account {phone}...\033[0m")
        try:
            client = TelegramClient(f'sessions/{phone}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            client.connect()
            
            if not client.is_user_authorized():
                print(f'\033[91m{phone} is not authorized. Exiting...\033[0m')
                return

            if '/joinchat/' in group_link:
                invite_hash = group_link.split('/joinchat/')[1]
                client(ImportChatInviteRequest(invite_hash))
            else:
                client(JoinChannelRequest(group_link))
            print(f"\033[92mSuccessfully joined the group with account {phone}\033[0m")
        except UserAlreadyParticipantError:
            print(f'\033[93mAccount {phone} is already a participant.\033[0m')
        except Exception as e:
            print(f'\033[91mFailed to join group with account {phone}: {e}\033[0m')
        finally:
            client.disconnect()

    elif choice == "2":
        for account in accounts:
            phone = account[0]
            print(f"\033[92mJoining the group with account {phone}...\033[0m")
            client = TelegramClient(f'sessions/{phone}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            client.connect()
            
            if not client.is_user_authorized():
                print(f'\033[91m{phone} is not authorized. Skipping...\033[0m')
                continue

            try:
                if '/joinchat/' in group_link:
                    invite_hash = group_link.split('/joinchat/')[1]
                    client(ImportChatInviteRequest(invite_hash))
                else:
                    client(JoinChannelRequest(group_link))
                print(f"\033[92mSuccessfully joined the group with account {phone}\033[0m")
            except UserAlreadyParticipantError:
                print(f'\033[93mAccount {phone} is already a participant.\033[0m')
            except Exception as e:
                print(f'\033[91mFailed to join group with account {phone}: {e}\033[0m')
            finally:
                client.disconnect()
            time.sleep(2)
    else:
        print("\033[91mInvalid choice. Exiting...\033[0m")

from telethon.tl.functions.channels import LeaveChannelRequest

def group_leaver():
    def banner():
        b = [
            '\033[92m░█████╗░██████╗░██████╗░███████╗██████╗░\033[0m',
            '\033[92m██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗\033[0m',
            '\033[92m███████║██║░░██║██║░░██║█████╗░░██████╔╝\033[0m',
            '\033[92m██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗\033[0m',
            '\033[92m██║░░██║██████╔╝██████╔╝███████╗██║░░██║\033[0m',
            '\033[92m╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝\033[0m'
        ]
        for char in b:
            print(char)
        print('\033[93mContact below address for get premium script\033[0m')
        print('\033[93mVersion: 2.0 | GitHub: @Scrapeleet\033[0m')
        print('\033[93mTelegram: @Scrapeleet | Instagram: @Scrapeleet\n\033[0m')

    def load_accounts():
        accounts = []
        with open('vars.txt', 'rb') as f:
            while True:
                try:
                    accounts.append(pickle.load(f))
                except EOFError:
                    break
        return accounts

    group_link = input("\033[96mEnter the group link you want the accounts to leave: \033[0m")
    accounts = load_accounts()
    print(f'\033[94mTotal accounts: {len(accounts)}\033[0m')

    print("\033[96mChoose an option:\033[0m")
    print("\033[96m1. Leave with one account\033[0m")
    print("\033[96m2. Leave with all accounts\033[0m")
    choice = input("\033[96mEnter your choice (1/2): \033[0m")

    if choice == "1":
        phone = accounts[0][0]
        print(f"\033[92mLeaving the group with account {phone}...\033[0m")
        try:
            client = TelegramClient(f'sessions/{phone}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            client.connect()
            
            if not client.is_user_authorized():
                print(f'\033[91m{phone} is not authorized. Exiting...\033[0m')
                return

            client(LeaveChannelRequest(group_link))
            print(f"\033[92mSuccessfully left the group with account {phone}\033[0m")
        except Exception as e:
            print(f'\033[91mFailed to leave group with account {phone}: {e}\033[0m')
        finally:
            client.disconnect()

    elif choice == "2":
        for account in accounts:
            phone = account[0]
            print(f"\033[92mLeaving the group with account {phone}...\033[0m")
            client = TelegramClient(f'sessions/{phone}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            client.connect()
            
            if not client.is_user_authorized():
                print(f'\033[91m{phone} is not authorized. Skipping...\033[0m')
                continue

            try:
                client(LeaveChannelRequest(group_link))
                print(f"\033[92mSuccessfully left the group with account {phone}\033[0m")
            except Exception as e:
                print(f'\033[91mFailed to leave group with account {phone}: {e}\033[0m')
            finally:
                client.disconnect()
            time.sleep(2)
    else:
        print("\033[91mInvalid choice. Exiting...\033[0m")




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
    auto_join_group_smmleet()
    time.sleep(5)
    print("Checking Verification Done\n")

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


    # Fetch groups from all accounts
    def fetch_groups():
        group_list = []
        for account in accounts:
            phn = account[0]
            clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            clnt.connect()
            dialogs = clnt.get_dialogs()
            for dialog in dialogs:
                if dialog.is_group or dialog.is_channel:
                    group_list.append({'title': dialog.name, 'id': dialog.id})
            clnt.disconnect()
        return group_list


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
    # Check if status file exists for resuming scraping
    try:
        with open('status.dat', 'rb') as f:
            status = pickle.load(f)
            f.close()
            resume_choice = input(f'{INPUT}{cy} Resume scraping online members from group {w}{status[0]}{lg}? [y/n]: {r}')
            if 'y' in resume_choice.lower():
                scraped_grp = status[0]
                index = int(status[1])
            else:
                if os.name == 'nt':
                    os.system('del status.dat')
                else:
                    os.system('rm status.dat')
                index = 0
                print(f'{info}{lg} Please select a new group to scrape online members from.{rs}')
        all_groups = fetch_groups()
        if not all_groups:
            print(f'{error} No groups found across accounts.')
            exit_window()

        print(f'{info} Fetched groups:')
        for idx, group in enumerate(all_groups, start=1):
            print(f'{idx}. {group["title"]}')
        group_choice = int(input(f'{INPUT}{cy} Select a group by number: {r}'))
        scraped_grp = all_groups[group_choice - 1]['id']

    except FileNotFoundError:
        print(f'{info}{lg} Please select a group to scrape online members from.{rs}')
        all_groups = fetch_groups()
        if not all_groups:
            print(f'{error} No groups found across accounts.')
            exit_window()

        print(f'{info} Fetched groups:')
        for idx, group in enumerate(all_groups, start=1):
            print(f'{idx}. {group["title"]}')
        group_choice = int(input(f'{INPUT}{cy} Select a group by number: {r}'))
        scraped_grp = all_groups[group_choice - 1]['id']
        index = 0


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
    status_choice = str(input(f'{INPUT}{cy} Do you wanna add online members?[y/n]: {r}'))
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

    # Get source group entity
    try:
        with open('status.dat', 'rb') as f:
            status = pickle.load(f)
            f.close()
            resume_choice = input(f'{INPUT}{cy} Resume scraping members from group {w}{status[0]}{lg}? [y/n]: {r}')
            if 'y' in resume_choice.lower():
                scraped_grp = status[0]
                index = int(status[1])
            else:
                if os.name == 'nt':
                    os.system('del status.dat')
                else:
                    os.system('rm status.dat')
                index = 0
    except FileNotFoundError:
        index = 0

    # Get the source group from which to scrape members
    if not scraped_grp:
        print(f'{info}{lg} Please select a group to scrape members from.{rs}')
        all_groups = fetch_groups()
        if not all_groups:
            print(f'{error} No groups found across accounts.')
            exit_window()

        print(f'{info} Fetched groups:')
        for idx, group in enumerate(all_groups, start=1):
            print(f'{idx}. {group["title"]}')
        group_choice = int(input(f'{INPUT}{cy} Select a group by number: {r}'))
        scraped_grp = all_groups[group_choice - 1]['id']

    for acc in to_use:
        stop = index + 60
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- Starting session... ')
        c.start(acc[0])
        acc_name = c.get_me().first_name
        try:
            # Handle source group joining
            if isinstance(scraped_grp, str) and '/joinchat/' in scraped_grp:
                g_hash = scraped_grp.split('/joinchat/')[1]
                try:
                    c(ImportChatInviteRequest(g_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined source group')
                except UserAlreadyParticipantError:
                    pass 
            else:
                try:
                    scraped_grp_entity = c.get_entity(scraped_grp)
                    c(JoinChannelRequest(scraped_grp_entity))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined source group')
                except UserAlreadyParticipantError:
                    pass

            # Handle target group joining
            if choice == 0:
                try:
                    target_entity = c.get_entity(target)
                    c(JoinChannelRequest(target_entity))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined target group')
                    target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
                except UserAlreadyParticipantError:
                    target_entity = c.get_entity(target)
                    target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
            else:
                try:
                    grp_hash = target.split('/joinchat/')[1]
                    c(ImportChatInviteRequest(grp_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined target group')
                    target_entity = c.get_entity(target)
                    target_details = target_entity
                except UserAlreadyParticipantError:
                    target_entity = c.get_entity(target)
                    target_details = target_entity

            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Retrieving entities...')
            
            # Get members from source group
            members = []
            try:
                members = c.get_participants(scraped_grp_entity, aggressive=False)
            except Exception as e:
                print(f'{error}{r} Couldn\'t scrape members')
                print(f'{error}{r} {e}')
                continue

            approx_members_count = len(members)
            if approx_members_count == 0:
                print(f'{error}{lg} No members found!')
                continue

            print(f'{info}{lg} Start: {w}{index}')
            adding_status = 0
            peer_flood_status = 0

            # Add members to target group
            for user in members[index:stop]:
                index += 1
                if user.bot:
                    continue
                try:
                    c(InviteToChannelRequest(target_details, [user]))
                    print(f'{success}{lg} User: {cy}{acc_name}{lg} -- Added member {cy}{user.username}')
                    adding_status += 1
                    time.sleep(sleep_time)
                except (UserAlreadyParticipantError, UserPrivacyRestrictedError,
                        ChatWriteForbiddenError, PeerFloodError, ChatAdminRequiredError,
                        FloodWaitError) as e:
                    print(f'{error}{r} Error: {str(e)}')
                    if isinstance(e, PeerFloodError):
                        peer_flood_status += 1
                        if peer_flood_status == 5:
                            print(f'{info}{lg} Rate limited, waiting 60 seconds...')
                            time.sleep(60)
                    elif isinstance(e, FloodWaitError):
                        print(f'{error}{cy} Flood wait error! Sleeping 15 seconds...')
                        time.sleep(15)
                    continue
                
                if stop == approx_members_count or index >= approx_members_count:
                    break

        except Exception as e:
            print(f'{error}{r} User: {cy}{acc_name}{lg} -- Failed to process')
            print(f'{error} {r}{e}')
            continue

        if adding_status > 0:
            log_status(scraped_grp, index)
            print(f'{info}{lg} Successfully added {w}{adding_status} members{lg} from account {w}{acc_name}')
        
        c.disconnect()
        print(f'{grey}-' * 50)

    print(f'{info}{lg} Finished adding online members!{rs}')

# def fetch_and_add_online_members() new:
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

#     group_joiner()

#     def fetch_all_groups():
#         all_groups = []
#         for acc in accounts:
#             try:
#                 client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#                 client.connect()
#                 client.start(acc[0])
#                 print(f'{info}{lg} Fetching groups from {client.get_me().first_name}...')
                
#                 dialogs = client.get_dialogs()
#                 for dialog in dialogs:
#                     if dialog.is_group or dialog.is_channel:
#                         group_info = {
#                             'id': dialog.entity.id,
#                             'title': dialog.entity.title,
#                             'access_hash': dialog.entity.access_hash,
#                             'members_count': getattr(dialog.entity, 'participants_count', 0),
#                             'username': getattr(dialog.entity, 'username', None)
#                         }
#                         if group_info not in all_groups:  # Avoid duplicates
#                             all_groups.append(group_info)
                
#                 client.disconnect()
#             except Exception as e:
#                 print(f'{error}{r} Failed to fetch groups from account {acc[0]}: {e}')
#                 continue
#         return all_groups

#     # Initialization and user input
#     accounts = []
#     with open('vars.txt', 'rb') as f:
#         while True:
#             try:
#                 accounts.append(pickle.load(f))
#             except EOFError:
#                 break

#     print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
    
#     # Fetch and display all groups
#     print(f'{info}{lg} Fetching all groups from all accounts...')
#     all_groups = fetch_all_groups()
    
#     if not all_groups:
#         print(f'{error}{r} No groups found!')
#         return

#     # Display groups for source selection
#     print(f'\n{info}{lg} Available groups to scrape from:')
#     for idx, group in enumerate(all_groups, 1):
#         member_count = f"({group['members_count']} members)" if group['members_count'] else ""
#         print(f"{idx}. {group['title']} {member_count}")

#     # Get source group selection
#     while True:
#         try:
#             source_choice = int(input(f'\n{INPUT}{cy} Select group to scrape online members from (1-{len(all_groups)}): {r}'))
#             if 1 <= source_choice <= len(all_groups):
#                 scraped_grp = all_groups[source_choice - 1]
#                 break
#             print(f'{error}{r} Invalid selection. Please try again.')
#         except ValueError:
#             print(f'{error}{r} Please enter a valid number.')

#     # Display groups for target selection
#     print(f'\n{info}{lg} Select target group to add members:')
#     for idx, group in enumerate(all_groups, 1):
#         member_count = f"({group['members_count']} members)" if group['members_count'] else ""
#         print(f"{idx}. {group['title']} {member_count}")

#     # Get target group selection
#     while True:
#         try:
#             target_choice = int(input(f'\n{INPUT}{cy} Select group to add members to (1-{len(all_groups)}): {r}'))
#             if 1 <= target_choice <= len(all_groups):
#                 target_grp = all_groups[target_choice - 1]
#                 break
#             print(f'{error}{r} Invalid selection. Please try again.')
#         except ValueError:
#             print(f'{error}{r} Please enter a valid number.')

#     sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request: {r}'))

#     # Process each account
#     for acc in accounts:
#         client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         client.connect()
#         client.start(acc[0])
#         print(f'{info}{lg} Logged in as {client.get_me().first_name}')

#         # Create source group entity
#         try:
#             scraped_grp_entity = InputPeerChannel(scraped_grp['id'], scraped_grp['access_hash'])
#             members = client.get_participants(scraped_grp_entity, aggressive=False)
#             online_members = [
#                 m for m in members
#                 if isinstance(m.status, UserStatusOnline)
#             ]
#         except Exception as e:
#             print(f'{error}{r} Failed to fetch members: {e}')
#             continue

#         print(f'{info}{lg} Found {w}{len(online_members)}{lg} online members.')

#         # Create target group entity
#         try:
#             target_details = InputPeerChannel(target_grp['id'], target_grp['access_hash'])
#         except Exception as e:
#             print(f'{error}{r} Failed to access target group: {e}')
#             continue

#         # Adding online members to target group
#         for user in online_members:
#             if user.bot:
#                 continue
#             try:
#                 client(InviteToChannelRequest(target_details, [user]))
#                 print(f'{success}{lg} Added member: {w}{user.username or user.id}')
#                 time.sleep(sleep_time)
#             except UserPrivacyRestrictedError:
#                 print(f'{error}{r} User has privacy restrictions')
#             except UserAlreadyParticipantError:
#                 print(f'{error}{r} User is already in the group')
#             except PeerFloodError:
#                 print(f'{error}{r} Too many requests, sleeping for 60 seconds')
#                 time.sleep(60)
#             except Exception as e:
#                 print(f'{error}{r} Failed to add member: {e}')
#                 continue

#         client.disconnect()
#         print(f'{info}{lg} Finished processing account: {acc[0]}')

#     print(f'{success}{lg} All online members added successfully!{rs}')

# def fetch_and_add_online_members():
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

#     # Initialization and user input
#     accounts = []
#     with open('vars.txt', 'rb') as f:
#         while True:
#             try:
#                 accounts.append(pickle.load(f))
#             except EOFError:
#                 break

#     print(f'{info}{lg} Total accounts: {w}{len(accounts)}')

#     groups = {}
#     for acc in accounts:
#         client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         client.connect()
#         client.start(acc[0])
#         print(f'{info}{lg} Logged in as {client.get_me().first_name}')

#         try:
#             dialogs = client.get_dialogs()
#             for dialog in dialogs:
#                 if dialog.is_group or dialog.is_channel:
#                     entity = dialog.entity
#                     if hasattr(entity, 'access_hash'):
#                         groups[f"{entity.id}:{entity.access_hash}"] = dialog.name
#         except Exception as e:
#             print(f'{error}{r} Failed to fetch groups for {acc[0]}: {e}')
#             client.disconnect()
#             continue

#         client.disconnect()

#     if not groups:
#         print(f'{error}{r} No groups found for any account.')
#         return

#     print(f'\n{info}{lg} Available Groups:')
#     for i, (grp_key, grp_name) in enumerate(groups.items(), start=1):
#         print(f'{i}. {grp_name}')
    
#     selected_group_idx = int(input(f'\n{INPUT}{cy} Select the group to scrape online members from (Enter number): {r}'))
#     selected_group_key = list(groups.keys())[selected_group_idx - 1]
#     selected_group_id, selected_group_hash = map(int, selected_group_key.split(':'))

#     target_grp = input(f'{INPUT}{cy} Enter group URL to add members: {r}')
#     sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request: {r}'))

#     for acc in accounts:
#         client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         client.connect()
#         client.start(acc[0])
#         print(f'{info}{lg} Logged in as {client.get_me().first_name}')

#         # Fetching only online members
#         try:
#             scraped_grp_entity = InputPeerChannel(selected_group_id, selected_group_hash)
#             members = client.get_participants(scraped_grp_entity, aggressive=False)
#             online_members = [
#                 m for m in members
#                 if isinstance(m.status, UserStatusOnline)  # Check if the user is online
#             ]
#         except Exception as e:
#             print(f'{error}{r} Failed to fetch members: {e}')
#             continue

#         print(f'{info}{lg} Found {w}{len(online_members)}{lg} online members.')

#         # Joining the target group
#         try:
#             if '/joinchat/' in target_grp:
#                 invite_hash = target_grp.split('/joinchat/')[1]
#                 client(ImportChatInviteRequest(invite_hash))
#             else:
#                 client(JoinChannelRequest(target_grp))
#             target_entity = client.get_entity(target_grp)
#             target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
#         except Exception as e:
#             print(f'{error}{r} Failed to join target group: {e}')
#             continue

#         # Adding online members to target group
#         for user in online_members:
#             if user.bot:
#                 continue
#             try:
#                 client(InviteToChannelRequest(target_details, [user]))
#                 print(f'{success}{lg} Added member: {w}{user.username or user.id}')
#                 time.sleep(sleep_time)
#             except Exception as e:
#                 print(f'{error}{r} Failed to add member: {e}')
#                 continue

#         client.disconnect()
#         print(f'{info}{lg} Finished processing account: {acc[0]}')

#     print(f'{success}{lg} All online members added successfully!{rs}')


# Self Joined Groups

# Initialize colorama
init()

# Color shortcuts
r = Fore.RED
lg = Fore.LIGHTGREEN_EX
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW

# Styled markers
info = f'{lg}[{w}i{lg}]{rs}'
error = f'{lg}[{r}!{lg}]{rs}'
success = f'{w}[{lg}*{w}]{rs}'
INPUT = f'{lg}[{cy}~{lg}]{rs}'

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


    # Fetch groups from all accounts
    def fetch_groups():
        group_list = []
        for account in accounts:
            phn = account[0]
            clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
            clnt.connect()
            dialogs = clnt.get_dialogs()
            for dialog in dialogs:
                if dialog.is_group or dialog.is_channel:
                    group_list.append({'title': dialog.name, 'id': dialog.id})
            clnt.disconnect()
        return group_list


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
    # Check if status file exists for resuming scraping
    try:
        with open('status.dat', 'rb') as f:
            status = pickle.load(f)
            f.close()
            resume_choice = input(f'{INPUT}{cy} Resume scraping members from group {w}{status[0]}{lg}? [y/n]: {r}')
            if 'y' in resume_choice.lower():
                scraped_grp = status[0]
                index = int(status[1])
            else:
                if os.name == 'nt':
                    os.system('del status.dat')
                else:
                    os.system('rm status.dat')
                index = 0
                print(f'{info}{lg} Please select a new group to scrape members from.{rs}')
        all_groups = fetch_groups()
        if not all_groups:
            print(f'{error} No groups found across accounts.')
            exit_window()

        print(f'{info} Fetched groups:')
        for idx, group in enumerate(all_groups, start=1):
            print(f'{idx}. {group["title"]}')
        group_choice = int(input(f'{INPUT}{cy} Select a group by number: {r}'))
        scraped_grp = all_groups[group_choice - 1]['id']

    except FileNotFoundError:
        print(f'{info}{lg} Please select a group to scrape members from.{rs}')
        all_groups = fetch_groups()
        if not all_groups:
            print(f'{error} No groups found across accounts.')
            exit_window()

        print(f'{info} Fetched groups:')
        for idx, group in enumerate(all_groups, start=1):
            print(f'{idx}. {group["title"]}')
        group_choice = int(input(f'{INPUT}{cy} Select a group by number: {r}'))
        scraped_grp = all_groups[group_choice - 1]['id']
        index = 0


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

    # Get source group entity
    try:
        with open('status.dat', 'rb') as f:
            status = pickle.load(f)
            f.close()
            resume_choice = input(f'{INPUT}{cy} Resume scraping members from group {w}{status[0]}{lg}? [y/n]: {r}')
            if 'y' in resume_choice.lower():
                scraped_grp = status[0]
                index = int(status[1])
            else:
                if os.name == 'nt':
                    os.system('del status.dat')
                else:
                    os.system('rm status.dat')
                index = 0
    except FileNotFoundError:
        index = 0

    # Get the source group from which to scrape members
    if not scraped_grp:
        print(f'{info}{lg} Please select a group to scrape members from.{rs}')
        all_groups = fetch_groups()
        if not all_groups:
            print(f'{error} No groups found across accounts.')
            exit_window()

        print(f'{info} Fetched groups:')
        for idx, group in enumerate(all_groups, start=1):
            print(f'{idx}. {group["title"]}')
        group_choice = int(input(f'{INPUT}{cy} Select a group by number: {r}'))
        scraped_grp = all_groups[group_choice - 1]['id']

    for acc in to_use:
        stop = index + 60
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- Starting session... ')
        c.start(acc[0])
        acc_name = c.get_me().first_name
        try:
            # Handle source group joining
            if isinstance(scraped_grp, str) and '/joinchat/' in scraped_grp:
                g_hash = scraped_grp.split('/joinchat/')[1]
                try:
                    c(ImportChatInviteRequest(g_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined source group')
                except UserAlreadyParticipantError:
                    pass 
            else:
                try:
                    scraped_grp_entity = c.get_entity(scraped_grp)
                    c(JoinChannelRequest(scraped_grp_entity))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined source group')
                except UserAlreadyParticipantError:
                    pass

            # Handle target group joining
            if choice == 0:
                try:
                    target_entity = c.get_entity(target)
                    c(JoinChannelRequest(target_entity))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined target group')
                    target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
                except UserAlreadyParticipantError:
                    target_entity = c.get_entity(target)
                    target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
            else:
                try:
                    grp_hash = target.split('/joinchat/')[1]
                    c(ImportChatInviteRequest(grp_hash))
                    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined target group')
                    target_entity = c.get_entity(target)
                    target_details = target_entity
                except UserAlreadyParticipantError:
                    target_entity = c.get_entity(target)
                    target_details = target_entity

            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Retrieving entities...')
            
            # Get members from source group
            members = []
            try:
                members = c.get_participants(scraped_grp_entity, aggressive=False)
            except Exception as e:
                print(f'{error}{r} Couldn\'t scrape members')
                print(f'{error}{r} {e}')
                continue

            approx_members_count = len(members)
            if approx_members_count == 0:
                print(f'{error}{lg} No members found!')
                continue

            print(f'{info}{lg} Start: {w}{index}')
            adding_status = 0
            peer_flood_status = 0

            # Add members to target group
            for user in members[index:stop]:
                index += 1
                if user.bot:
                    continue
                try:
                    c(InviteToChannelRequest(target_details, [user]))
                    print(f'{success}{lg} User: {cy}{acc_name}{lg} -- Added member {cy}{user.username}')
                    adding_status += 1
                    time.sleep(sleep_time)
                except (UserAlreadyParticipantError, UserPrivacyRestrictedError,
                        ChatWriteForbiddenError, PeerFloodError, ChatAdminRequiredError,
                        FloodWaitError) as e:
                    print(f'{error}{r} Error: {str(e)}')
                    if isinstance(e, PeerFloodError):
                        peer_flood_status += 1
                        if peer_flood_status == 5:
                            print(f'{info}{lg} Rate limited, waiting 60 seconds...')
                            time.sleep(60)
                    elif isinstance(e, FloodWaitError):
                        print(f'{error}{cy} Flood wait error! Sleeping 15 seconds...')
                        time.sleep(15)
                    continue
                
                if stop == approx_members_count or index >= approx_members_count:
                    break

        except Exception as e:
            print(f'{error}{r} User: {cy}{acc_name}{lg} -- Failed to process')
            print(f'{error} {r}{e}')
            continue

        if adding_status > 0:
            log_status(scraped_grp, index)
            print(f'{info}{lg} Successfully added {w}{adding_status} members{lg} from account {w}{acc_name}')
        
        c.disconnect()
        print(f'{grey}-' * 50)

    print(f'{info}{lg} Finished adding members!{rs}')



# def start_scraping_and_adding():
#     def banner():
#         b = [
#             f'{cy}░█████╗░██████╗░██████╗░███████╗██████╗░',
#             f'{cy}██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗',
#             f'{cy}███████║██║░░██║██║░░██║█████╗░░██████╔╝',
#             f'{cy}██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗',
#             f'{cy}██║░░██║██████╔╝██████╔╝███████╗██║░░██║',
#             f'{cy}╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝{rs}'
#         ]
#         for char in b:
#             print(char)
#         print(f'{lg}Contact below address for premium scripts{rs}')

#     def clr():
#         if os.name == 'nt':
#             os.system('cls')
#         else:
#             os.system('clear')

#     clr()
#     banner()

#     accounts = []
#     with open('vars.txt', 'rb') as f:
#         while True:
#             try:
#                 accounts.append(pickle.load(f))
#             except EOFError:
#                 break

#     print(f'{info} Total accounts: {len(accounts)}')
#     number_of_accs = int(input(f'{INPUT} {cy}How Many Accounts You Want to Use In Adding:{rs} '))
#     to_use = accounts[:number_of_accs]

#     group_link = input(f'{INPUT} {cy}Enter the link of the group to add members to:{rs} ')

#     for acc in to_use:
#         try:
#             print(f'{info} {lg}Using account: {acc[0]}{rs}')
#             with TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6') as c:
#                 try:
#                     target_grp_entity = c.get_entity(group_link)
#                     c(JoinChannelRequest(target_grp_entity))
#                     print(f'{success} {lg}{acc[0]}{rs} joined the group {cy}{group_link}{rs}')
#                     time.sleep(3)
#                 except ChannelInvalidError:
#                     print(f'{error} Invalid group link or account restrictions for {lg}{acc[0]}{rs}')
#                     continue  # Move to the next account
#                 except FloodWaitError as e:
#                     print(f'{error} FloodWaitError: Must wait {ye}{e.seconds}{rs} seconds for {lg}{acc[0]}{rs}')
#                     continue  # Skip to the next account
#                 except Exception as e:
#                     print(f'{error} Error joining group for {lg}{acc[0]}{rs}: {r}{e}{rs}')
#                     continue  # Skip to the next account

#                 dialogs = c.get_dialogs()
#                 groups = [d for d in dialogs if d.is_group or d.is_channel]
#                 print(f'\n{info} {cy}Available groups for {lg}{acc[0]}{rs}:')

#                 for i, group in enumerate(groups):
#                     print(f'{lg}{i + 1}.{rs} {w}{group.title}{rs}')

#                 group_index = int(input(f'{INPUT} {cy}Select a group to scrape members from (1-{len(groups)}):{rs} ')) - 1
#                 scraped_grp = groups[group_index]

#                 members = c.get_participants(scraped_grp, aggressive=True)
#                 print(f'{info} {lg}Scraped {cy}{len(members)}{lg} members from {cy}{scraped_grp.title}{rs}')

#                 delay_time = int(input(f'{INPUT} {cy}Enter delay time per request [0 for None]:{rs} '))

#                 for member in members:
#                     try:
#                         c(InviteToChannelRequest(target_grp_entity, [member]))
#                         print(f'{success} Added member {cy}{member.username or member.id}{rs}')
#                         if delay_time > 0:
#                             time.sleep(delay_time)
#                     except UserPrivacyRestrictedError:
#                         print(f'{error} Privacy restrictions for {cy}{member.username or member.id}{rs}')
#                     except FloodWaitError as e:
#                         print(f'{error} FloodWaitError: Must wait {ye}{e.seconds}{rs} seconds')
#                         break  # Skip to the next account
#                     except Exception as e:
#                         print(f'{error} Error adding {cy}{member.username or member.id}{rs}: {r}{e}{rs}')
#                         time.sleep(5)
#         except Exception as e:
#             print(f'{error} Critical error with account {lg}{acc[0]}{rs}: {r}{e}{rs}')
#             continue  # Skip to the next account

#     print(f'{info} {lg}Finished adding members!{rs}')







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
    print("\nIf the group you want to scrape messages from has security verification,")
    print("you'll need to join the group manually.")
    print("Complete the verification process by answering the required questions before proceeding with message scraping.")
    target = input(f'\n{INPUT}{cy} Enter group URL link to move messages to: {r}')
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
    print('Adding Account To Scrapeleet Channels in case you wanna speak to us')
    auto_join_group()
    print('All Account added successfully to Scrapeleet group\n')

    print("Loading and Checking for verifications")
    auto_join_group_smmleet()
    time.sleep(5)
    print("Checking Verification Done\n")

    scraped_grp = input(f'{INPUT}{cy} Public/Private group URL link to scrape messages: {r}')
    print("\nIf the group you want to scrape messages from has security verification,")
    print("you'll need to join the group manually.")
    print("Complete the verification process by answering the required questions before proceeding with message scraping.")
    target = input(f'\n{INPUT}{cy} Enter group URL link to move messages to: {r}')
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

    print("\nIf the group you want to scrape messages from has security verification,")
    print("you'll need to join the group manually.")
    print("Complete the verification process by answering the required questions before proceeding with message scraping.")

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


# import os
# import pickle
# import random
# import sys
# import time
# from telethon import TelegramClient, events
# from telethon.errors import PhoneNumberBannedError, UserAlreadyParticipantError
# from telethon.tl.functions.channels import JoinChannelRequest
# from telethon.tl.functions.messages import ImportChatInviteRequest
# from telethon.tl.functions.channels import InviteToChannelRequest
# from telethon.tl.types import InputUser
# from telethon.tl.types import InputPeerChannel
# from colorama import Fore, Style, init

# # Initialize colorama
# init(autoreset=True)

# # Function to display a banner
# def banner():
#     banner_text = [
#         f"{Fore.RED}░█████╗░{Fore.GREEN}██████╗░{Fore.BLUE}██████╗░{Fore.YELLOW}███████╗{Fore.CYAN}██████╗░",
#         f"{Fore.RED}██╔══██╗{Fore.GREEN}██╔══██╗{Fore.BLUE}██╔══██╗{Fore.YELLOW}██╔════╝{Fore.CYAN}██╔══██╗",
#         f"{Fore.RED}███████║{Fore.GREEN}██║░░██║{Fore.BLUE}██║░░██║{Fore.YELLOW}█████╗░░{Fore.CYAN}██████╔╝",
#         f"{Fore.RED}██╔══██║{Fore.GREEN}██║░░██║{Fore.BLUE}██║░░██║{Fore.YELLOW}██╔══╝░░{Fore.CYAN}██╔══██╗",
#         f"{Fore.RED}██║░░██║{Fore.GREEN}██████╔╝{Fore.BLUE}██████╔╝{Fore.YELLOW}███████╗{Fore.CYAN}██║░░██║",
#         f"{Fore.RED}╚═╝░░╚═╝{Fore.GREEN}╚═════╝░{Fore.BLUE}╚═════╝░{Fore.YELLOW}╚══════╝{Fore.CYAN}╚═╝░░╚═╝"
#     ]
#     for line in banner_text:
#         print(line)
#     print(f"{Fore.MAGENTA}Contact below address for premium script")
#     print(f"{Fore.CYAN}Version: 2.0 | GitHub: @Scrapeleet")
#     print(f"{Fore.CYAN}Telegram: @Scrapeleet | Instagram: @Scrapeleet\n")

# # Function to clear the screen
# def clr():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # Fetch a limited number of group messages and extract user details
# def fetch_group_messages(client, group_id, max_members):
#     print(f"{Fore.GREEN}Fetching messages and extracting member details...")
#     user_details = []

#     async def get_messages():
#         async for message in client.iter_messages(group_id, limit=max_members):
#             if message.sender_id and message.sender:
#                 user_details.append((message.sender_id, message.sender.access_hash))
    
#     client.loop.run_until_complete(get_messages())
#     print(f"{Fore.YELLOW}Extracted {len(user_details)} user details.")
#     return user_details

# def hidden_members():
#     clr()
#     banner()

#     accounts = []
#     with open('vars.txt', 'rb') as f:
#         while True:
#             try:
#                 accounts.append(pickle.load(f))
#             except EOFError:
#                 break

#     print(f"{Fore.CYAN}Checking for banned accounts...")
#     for a in accounts[:]:
#         phn = a[0]
#         client = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         client.connect()
#         if not client.is_user_authorized():
#             try:
#                 client.send_code_request(phn)
#             except PhoneNumberBannedError:
#                 print(f"{Fore.RED}{phn} is banned! Removing from accounts.")
#                 accounts.remove(a)
#         client.disconnect()

#     print(f"{Fore.CYAN}Enter the source group link to scrape hidden members:")
#     source_group_url = input(f"{Fore.YELLOW}Enter source group URL to scrape hidden member from: ")

#     max_members = int(input(f"{Fore.CYAN}Enter the number of members to scrape per each account(e.g 20 to 200): "))

#     print(f"{Fore.CYAN}Enter the target group details:")
#     target = input(f"{Fore.YELLOW}Enter public or private group URL to add members to: ")

#     delay = int(input(f"{Fore.CYAN}Enter delay time per request (suggested: 30): "))

#     print(f"{Fore.GREEN}Joining groups and adding members...")
#     for acc in accounts:
#         client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         client.start(acc[0])

#         # Join source group using the entered link
#         try:
#             client(ImportChatInviteRequest(source_group_url))
#             print(f"{Fore.GREEN}Joined source group with account {acc[0]}.")
#         except Exception as e:
#             print(f"{Fore.RED}Error joining source group: {e}")

#         # Scrape user details from messages
#         user_details = fetch_group_messages(client, source_group_url, max_members)

#         # Join target group
#         try:
#             target_entity = client.get_entity(target)
#             client(JoinChannelRequest(target_entity))
#             print(f"{Fore.GREEN}Joined target group with account {acc[0]}.")
#         except UserAlreadyParticipantError:
#             print(f"{Fore.YELLOW}Account {acc[0]} already in target group.")

#         # Add members to target group
#         for user_id, user_hash in user_details:
#             try:
#                 # Check if the user is already in the target group
#                 participants = client.get_participants(target_entity)
#                 participant_ids = [user.id for user in participants]
#                 if user_id in participant_ids:
#                     print(f"User {user_id} is already in the target group.")
#                     continue  # Skip adding this user

#                 user = InputUser(user_id, user_hash)  # Ensure the correct entity type
#                 response = client(InviteToChannelRequest(target_entity, [user]))
#                 if response:
#                     print(f"{Fore.YELLOW}Successfully added user {user_id} to target group.")
#                 else:
#                     print(f"Failed to add user {user_id} to target group.")
                
#                 time.sleep(delay)  # Respect API rate limits
#             except Exception as e:
#                 print(f"Error adding user {user_id}: {e}")
#         client.disconnect()



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
    # group_joiner()

    try:
        scraped_grp = input(f'{INPUT}{cy} Public/Private group URL to scrape members: {r}')
    except:
        print(f'{error} Failed to input group link!')
        return

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

    print(f'{info}{lg} Scraping members from the source group...')

    scraped_members = []
    
    # Ask for the number of messages to scrape
    max_messages = int(input(f'{INPUT}{cy} Enter the number of members to scrape per account: {r}'))

    for acc in accounts:
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        c.connect()
        try:
            scraped_grp_entity = c.get_entity(scraped_grp)
            c(JoinChannelRequest(scraped_grp_entity))
            print(f'{success}{lg} User {cy}{acc[0]} joined the source group successfully!{rs}')
        except UserAlreadyParticipantError:
            print(f'{info}{cy} User {acc[0]} is already a member of the source group!{rs}')
        except Exception as e:
            print(f'{error}{r} User {acc[0]} failed to join the source group. Error: {e}{rs}')
            c.disconnect()
            continue

        count = 0
        for message in c.iter_messages(scraped_grp_entity, reverse=True):
            if count >= max_messages:
                break
            if message.sender_id and message.sender_id not in scraped_members:
                scraped_members.append(message.sender_id)
                count += 1

        c.disconnect()

    print(f'{info}{lg} Total members scraped: {len(scraped_members)}')

    members_per_account = len(scraped_members) // number_of_accs
    split_members = [
        scraped_members[i * members_per_account:(i + 1) * members_per_account]
        for i in range(number_of_accs)
    ]

    for idx, acc in enumerate(accounts[:number_of_accs]):
        c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        c.connect()

        try:
            if choice == 0:
                target_entity = c.get_entity(target)
                c(JoinChannelRequest(target_entity))
            else:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                target_entity = c.get_entity(target)

            print(f'{success}{lg} User {cy}{acc[0]} joined the destination group successfully!{rs}')
        except UserAlreadyParticipantError:
            print(f'{info}{cy} User {acc[0]} is already a member of the destination group!{rs}')
        except Exception as e:
            print(f'{error}{r} User {acc[0]} failed to join the destination group. Error: {e}{rs}')
            c.disconnect()
            continue

        for user_id in split_members[idx]:
            try:
                user = c.get_entity(user_id)
                c(InviteToChannelRequest(target_entity, [user]))
                print(f'{success}{lg} Added member {cy}{user.username}')
                time.sleep(sleep_time)
            except UserAlreadyParticipantError:
                print(f'{info}{cy} User {cy}{user.username} already added!{rs}')
            except UserPrivacyRestrictedError:
                print(f'{info}{cy} User {cy}{user.username} has privacy restrictions!{rs}')
            except Exception as e:
                print(f'{error}{r} Failed to add user. Error: {e}')

        c.disconnect()

    print(f'{info}{lg} Finished adding members!{rs}')




# def hidden_members():
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
#         print('Contact below address for premium script')
#         print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
#         print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

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

#     try:
#         scraped_grp = input(f'{INPUT}{cy} Public/Private group URL to scrape members: {r}')
#     except:
#         print(f'{error} Failed to input group link!')
#         return

#     scrape_limit = int(input(f'{INPUT}{cy} Enter number of members to scrape per account (limit: 100): {r}'))

#     number_of_accs = int(input(f'{INPUT}{cy} How many accounts do you want to use for adding? {r}'))
#     print(f'{info}{cy} Choose an option{lg}')
#     print(f'{cy}[0]{lg} Add to public group')
#     print(f'{cy}[1]{lg} Add to private group')
#     choice = int(input(f'{INPUT}{cy} Enter choice: {r}'))

#     if choice == 0:
#         target = str(input(f'{INPUT}{cy} Enter public group URL link: {r}'))
#     else:
#         target = str(input(f'{INPUT}{cy} Enter private group URL link: {r}'))

#     sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request [suggest 30]: {r}'))

#     print(f'{info}{lg} Joining both groups from {w}{number_of_accs} accounts...')

#     for acc in accounts[:number_of_accs]:
#         c = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}Starting session...')
#         c.start(acc[0])

#         # Step 1: Join the source group
#         try:
#             scraped_grp_entity = c.get_entity(scraped_grp)
#             c(JoinChannelRequest(scraped_grp_entity))
#             print(f'{success}{lg} User {cy}{acc[0]} joined the source group successfully!{rs}')
#         except UserAlreadyParticipantError:
#             print(f'{info}{cy} User {acc[0]} is already a member of the source group!{rs}')
#         except Exception as e:
#             print(f'{error}{r} User {acc[0]} failed to join the source group. Error: {e}{rs}')
#             c.disconnect()
#             continue

#         # Step 2: Join the destination group
#         try:
#             if choice == 0:
#                 target_entity = c.get_entity(target)
#                 c(JoinChannelRequest(target_entity))
#             else:
#                 grp_hash = target.split('/joinchat/')[1]
#                 c(ImportChatInviteRequest(grp_hash))
#                 target_entity = c.get_entity(target)

#             print(f'{success}{lg} User {cy}{acc[0]} joined the destination group successfully!{rs}')
#         except UserAlreadyParticipantError:
#             print(f'{info}{cy} User {acc[0]} is already a member of the destination group!{rs}')
#         except Exception as e:
#             print(f'{error}{r} User {acc[0]} failed to join the destination group. Error: {e}{rs}')
#             c.disconnect()
#             continue

#         # Step 3: Scrape members and add to the destination group
#         try:
#             active_members = []
#             for message in c.iter_messages(scraped_grp_entity):
#                 if len(active_members) >= scrape_limit:
#                     break
#                 if message.sender_id:
#                     try:
#                         user = c.get_entity(message.sender_id)
#                         if user not in active_members:
#                             active_members.append(user)
#                     except Exception as e:
#                         print(f'{error}{r} Could not fetch user {message.sender_id}. Error: {e}')
#                         continue

#             print(f'{info}{lg} Retrieved {len(active_members)} active members!')

#             for user in active_members:
#                 try:
#                     c(InviteToChannelRequest(target_entity, [user]))
#                     print(f'{success}{lg} Added member {cy}{user.username}')
#                     time.sleep(sleep_time)
#                 except UserAlreadyParticipantError:
#                     print(f'{info}{cy} User {cy}{user.username} already added!{rs}')
#                 except UserPrivacyRestrictedError:
#                     print(f'{info}{cy} User {cy}{user.username} has privacy restrictions!{rs}')
#                 except Exception as e:
#                     print(f'{error}{r} Failed to add user. Error: {e}')
#         except Exception as e:
#             print(f'{error}{r} Could not process group. Error: {e}')
#         finally:
#             c.disconnect()
#             print(f'{grey}-' * 50)

#     print(f'{info}{lg} Finished adding active members!{rs}')



from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


# def scrape_hidden_members_from_groups():
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
#         print('Contact below address for premium script')
#         print(f'{lg}Version: {w}2.0{lg} | GitHub: {w}@Scrapeleet{rs}')
#         print(f'{lg}Telegram: {w}@Scrapeleet{lg} | Instagram: {w}@Scrapeleet{rs}\n')

#     def clr():
#         if os.name == 'nt':
#             os.system('cls')
#         else:
#             os.system('clear')

#     banner()

#     # Read accounts
#     accounts = []
#     with open('vars.txt', 'rb') as f:
#         while True:
#             try:
#                 accounts.append(pickle.load(f))
#             except EOFError:
#                 break

#     print(f'{info}{lg} Loaded {len(accounts)} accounts!')

#     scrape_limit = int(input(f'{INPUT}{cy} Enter the number of members to scrape per account (limit: 100): {r}'))
#     sleep_time = int(input(f'{INPUT}{cy} Enter delay time per request (suggest 30): {r}'))

#     # Fetch and display groups
#     source_group = None
#     for acc in accounts:
#         client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         client.start(acc[0])
#         print(f'{info}{lg} Logged in as {cy}{acc[0]}{rs}')
#         try:
#             # Fetch and display groups for selection
#             dialogs = client.get_dialogs()
#             groups = [dialog for dialog in dialogs if dialog.is_group or dialog.is_channel]
#             print(f'{info}{lg} Groups for account {cy}{acc[0]}:')
#             for i, group in enumerate(groups):
#                 print(f'{lg}[{i}] {group.name}')
#             choice = int(input(f'{INPUT}{cy} Select a group number to scrape members from: {r}'))
#             source_group = groups[choice].entity

#             # Scrape members
#             print(f'{info}{lg} Scraping members from {source_group.title}...')
#             members = client(GetParticipantsRequest(
#                 source_group,
#                 filter=ChannelParticipantsSearch(''),
#                 offset=0,
#                 limit=scrape_limit,
#                 hash=0
#             )).users

#             print(f'{success}{lg} Scraped {len(members)} members!')

#             # Prompt for target group and add members
#             target_group = input(f'{INPUT}{cy} Enter the target group URL or username to add members to: {r}')
#             target_entity = client.get_entity(target_group)

#             for member in members:
#                 try:
#                     client(InviteToChannelRequest(target_entity, [member]))
#                     print(f'{success}{lg} Added {cy}{member.username or member.id} to target group!{rs}')
#                     time.sleep(sleep_time)
#                 except UserAlreadyParticipantError:
#                     print(f'{info}{cy}{member.username or member.id} is already in the group.')
#                 except UserPrivacyRestrictedError:
#                     print(f'{error}{cy} Cannot add {member.username or member.id}. Privacy settings restrict this.')
#                 except Exception as e:
#                     print(f'{error}{r} Failed to add {member.username or member.id}. Error: {e}')
#         except Exception as e:
#             print(f'{error}{r} Could not process group. Error: {e}')
#         finally:
#             client.disconnect()
#             print(f'{grey}-' * 50)

#     print(f'{info}{lg} Completed adding members to the target group!{rs}')


from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


from telethon.sync import TelegramClient
from telethon.errors import UserAlreadyParticipantError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import GetParticipantsRequest, InviteToChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
import pickle
import time
from colorama import Fore, Style

# Color definitions
info = Fore.CYAN
success = Fore.GREEN
error = Fore.RED
input_color = Fore.YELLOW
reset = Style.RESET_ALL

def banner():
    print(f"{success}░█████╗░██████╗░██████╗░███████╗██████╗░{reset}")
    print(f"{success}██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗{reset}")
    print(f"{success}███████║██║░░██║██║░░██║█████╗░░██████╔╝{reset}")
    print(f"{success}██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗{reset}")
    print(f"{success}██║░░██║██████╔╝██████╔╝███████╗██║░░██║{reset}")
    print(f"{success}╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝{reset}")
    print(f"{info}Version: 2.0 | GitHub: @Scrapeleet{reset}")
    print(f"{info}Telegram: @Scrapeleet | Instagram: @Scrapeleet{reset}\n")

# Global set to track added members across all accounts
added_members = set()

import os
import pickle
import random
import sys
import time
from telethon import TelegramClient, events
from telethon.errors import PhoneNumberBannedError, UserAlreadyParticipantError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputUser
from telethon.tl.types import InputPeerChannel
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to display a banner
def banner():
    banner_text = [
        f"{Fore.RED}░█████╗░{Fore.GREEN}██████╗░{Fore.BLUE}██████╗░{Fore.YELLOW}███████╗{Fore.CYAN}██████╗░",
        f"{Fore.RED}██╔══██╗{Fore.GREEN}██╔══██╗{Fore.BLUE}██╔══██╗{Fore.YELLOW}██╔════╝{Fore.CYAN}██╔══██╗",
        f"{Fore.RED}███████║{Fore.GREEN}██║░░██║{Fore.BLUE}██║░░██║{Fore.YELLOW}█████╗░░{Fore.CYAN}██████╔╝",
        f"{Fore.RED}██╔══██║{Fore.GREEN}██║░░██║{Fore.BLUE}██║░░██║{Fore.YELLOW}██╔══╝░░{Fore.CYAN}██╔══██╗",
        f"{Fore.RED}██║░░██║{Fore.GREEN}██████╔╝{Fore.BLUE}██████╔╝{Fore.YELLOW}███████╗{Fore.CYAN}██║░░██║",
        f"{Fore.RED}╚═╝░░╚═╝{Fore.GREEN}╚═════╝░{Fore.BLUE}╚═════╝░{Fore.YELLOW}╚══════╝{Fore.CYAN}╚═╝░░╚═╝"
    ]
    for line in banner_text:
        print(line)
    print(f"{Fore.MAGENTA}Contact below address for premium script")
    print(f"{Fore.CYAN}Version: 2.0 | GitHub: @Scrapeleet")
    print(f"{Fore.CYAN}Telegram: @Scrapeleet | Instagram: @Scrapeleet\n")

# Function to clear the screen
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fetch a limited number of group messages and extract user details
def fetch_group_messages(client, group_id, max_members):
    print(f"{Fore.GREEN}Fetching messages and extracting member details...")
    user_details = []

    async def get_messages():
        async for message in client.iter_messages(group_id, limit=max_members):
            if message.sender_id and message.sender:
                user_details.append((message.sender_id, message.sender.access_hash))
    
    client.loop.run_until_complete(get_messages())
    print(f"{Fore.YELLOW}Extracted {len(user_details)} user details.")
    return user_details

def scrape_hidden_members_from_groups():
    clr()
    banner()

    accounts = []
    with open('vars.txt', 'rb') as f:
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

    print(f"{Fore.CYAN}Checking for banned accounts...")
    for a in accounts[:]:
        phn = a[0]
        client = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phn)
            except PhoneNumberBannedError:
                print(f"{Fore.RED}{phn} is banned! Removing from accounts.")
                accounts.remove(a)
        client.disconnect()

    print(f"{Fore.CYAN}Fetching groups...")
    groups = []
    for acc in accounts:
        phn = acc[0]
        client = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        client.connect()
        for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                groups.append({'title': dialog.name, 'id': dialog.id})
        client.disconnect()

    print(f"{Fore.GREEN}Available groups:")
    for idx, group in enumerate(groups, start=1):
        print(f"{Fore.YELLOW}{idx}. {group['title']}")

    group_choice = int(input(f"{Fore.CYAN}Select a group by number: "))
    selected_group = groups[group_choice - 1]['id']

    max_members = int(input(f"{Fore.CYAN}Enter the number of members to scrape per each account(e.g 20 to 500): "))

    print(f"{Fore.CYAN}Enter the target group details:")
    target = input(f"{Fore.YELLOW}Enter public or private group URL to add members to: ")

    delay = int(input(f"{Fore.CYAN}Enter delay time per request (suggested: 30): "))
    
    print(f"{Fore.GREEN}Joining groups and adding members...")
    for acc in accounts:
        client = TelegramClient(f'sessions/{acc[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
        client.start(acc[0])

        # Join source group
        try:
            client(JoinChannelRequest(selected_group))
            print(f"{Fore.GREEN}Joined source group with account {acc[0]}.")
        except UserAlreadyParticipantError:
            print(f"{Fore.YELLOW}Account {acc[0]} already in source group.")

        # Scrape user details from messages
        user_details = fetch_group_messages(client, selected_group, max_members)

        # Join target group
        try:
            target_entity = client.get_entity(target)
            client(JoinChannelRequest(target_entity))
            print(f"{Fore.GREEN}Joined target group with account {acc[0]}.")
        except UserAlreadyParticipantError:
            print(f"{Fore.YELLOW}Account {acc[0]} already in target group.")

        # Add members to target group
        for user_id, user_hash in user_details:
            try:
                # Check if the user is already in the target group
                participants = client.get_participants(target_entity)
                participant_ids = [user.id for user in participants]
                if user_id in participant_ids:
                    print(f"User {user_id} is already in the target group.")
                    continue  # Skip adding this user

                user = InputUser(user_id, user_hash)  # Ensure the correct entity type
                response = client(InviteToChannelRequest(target_entity, [user]))
                if response:
                    print(f"{Fore.YELLOW}Successfully added user {user_id} to target group.")
                else:
                    print(f"Failed to add user {user_id} to target group.")
                
                time.sleep(delay)  # Respect API rate limits
            except Exception as e:
                print(f"Error adding user {user_id}: {e}")
        client.disconnect()




# def scrape_hidden_members_from_groups():
#     banner()

#     group_joiner()

#     print(f"\n{info}Please ensure the following before starting:{reset}")
#     print(f"{success}Please make sure you add both the target group to scrape members from and the target group to add them to.{reset}")
#     print(f"{success}Add members manually before you continue this process\n{reset}")

#     # Load the account credentials
#     accounts = []
#     with open('vars.txt', 'rb') as f:
#         while True:
#             try:
#                 accounts.append(pickle.load(f))
#             except EOFError:
#                 break

#     if not accounts:
#         print(f"{error}No accounts found in vars.txt!{reset}")
#         return

#     print(f"{info}Loaded {len(accounts)} account(s).{reset}")
    
#     # Select the target group
#     target_group_url = input(f"{input_color}Enter the target group URL or username to add member to: {reset}")
    
#     # Scraping members from the groups using all accounts
#     for account in accounts:
#         client = TelegramClient(f'sessions/{account[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         client.start(account[0])

#         try:
#             print(f"{info}Joining the target group with account {account[0]}...{reset}")
#             target_group = client.get_entity(target_group_url)
            
#             # Ensure that target_group is a valid channel
#             if not target_group.megagroup and not target_group.broadcast:
#                 print(f"{error}The target group is not a valid channel.{reset}")
#                 continue

#             # Fetch available groups for scraping
#             dialogs = client.get_dialogs()  # Get dialogs using the current account
#             groups = [dialog for dialog in dialogs if dialog.is_group or dialog.is_channel]
#             if not groups:
#                 print(f"{error}No groups available in this account!{reset}")
#                 continue

#             # Display available groups
#             for i, group in enumerate(groups):
#                 print(f"{success}[{i}] {group.name}{reset}")
            
#             # Select the source group
#             source_group_index = int(input(f"{input_color}Enter the number of the source group: {reset}"))
#             source_group = groups[source_group_index].entity

#             # Scraping and adding members
#             scrape_limit = int(input(f"{input_color}Enter the number of members to scrape per account: {reset}"))
#             delay_time = int(input(f"{input_color}Enter the delay time per request (seconds): {reset}"))

#             print(f"{info}Scraping members from {source_group.title}...{reset}")
#             participants = client(GetParticipantsRequest(
#                 source_group,
#                 filter=ChannelParticipantsSearch(''),
#                 offset=0,
#                 limit=scrape_limit,
#                 hash=0
#             )).users

#             print(f"{success}Scraped {len(participants)} members. Adding them to {target_group.title}...{reset}")
#             for member in participants:
#                 try:
#                     client(InviteToChannelRequest(target_group, [member]))
#                     print(f"{success}Added {member.username or member.id} to the target group with account {account[0]}!{reset}")
#                     time.sleep(delay_time)
#                 except UserAlreadyParticipantError:
#                     print(f"{info}{member.username or member.id} is already in the group with account {account[0]}.{reset}")
#                 except UserPrivacyRestrictedError:
#                     print(f"{error}Cannot add {member.username or member.id} due to privacy settings with account {account[0]}.{reset}")
#                 except Exception as e:
#                     print(f"{error}Error adding {member.username or member.id} with account {account[0]}: {e}{reset}")

#         except Exception as e:
#             print(f"{error}An error occurred with account {account[0]}: {e}{reset}")
#             continue

#     print(f"{info}All operations completed.{reset}")






# def scrape_hidden_members_from_groups():
#     banner()

#     print(f"\n{r}Please ensure the following before starting:{rs}")
#     print(f"{cy}1. Add all accounts to destination groups.{rs}")
#     print(f"{cy}2. Add all accounts to target groups.{rs}\n")

#     # Load the account credentials
#     accounts = []
#     with open('vars.txt', 'rb') as f:
#         while True:
#             try:
#                 accounts.append(pickle.load(f))
#             except EOFError:
#                 break

#     if not accounts:
#         print(f"{error}No accounts found in vars.txt!{reset}")
#         return

#     print(f"{info}Loaded {len(accounts)} account(s).{reset}")
    
#     # Select the target group
#     target_group_url = input(f"{input_color}Enter the target group URL or username you want to add member to: {reset}")
    
#     # Start the client with each account and join the target group
#     for account in accounts:
#         client = TelegramClient(f'sessions/{account[0]}', 3910389, '86f861352f0ab76a251866059a6adbd6')
#         client.start(account[0])

#         try:
#             print(f"{info}Joining the target group with account {account[0]}...{reset}")
#             target_group = client.get_entity(target_group_url)
            
#             # Ensure that target_group is a valid channel
#             if not target_group.megagroup and not target_group.broadcast:
#                 print(f"{error}The target group is not a valid channel.{reset}")
#                 continue

#             # Add account to the target group
#             try:
#                 client(InviteToChannelRequest(target_group, [account[0]]))
#                 print(f"{success}Account {account[0]} added to the target group!{reset}")
#             except Exception as e:
#                 print(f"{error}Error adding account {account[0]}: {e}{reset}")
#                 continue

#         except Exception as e:
#             print(f"{error}An error occurred with account {account[0]}: {e}{reset}")
#             continue

#     # Now, after all accounts have joined the target group, proceed with member scraping and adding
#     # Fetch available groups for scraping
#     dialogs = client.get_dialogs()
#     groups = [dialog for dialog in dialogs if dialog.is_group or dialog.is_channel]
#     if not groups:
#         print(f"{error}No groups available in this account!{reset}")
#         return

#     # Display available groups
#     for i, group in enumerate(groups):
#         print(f"{success}[{i}] {group.name}{reset}")
    
#     # Select the source group
#     source_group_index = int(input(f"{input_color}Enter the number of the source group: {reset}"))
#     source_group = groups[source_group_index].entity

#     # Scraping and adding members
#     scrape_limit = int(input(f"{input_color}Enter the number of members to scrape per account: {reset}"))
#     delay_time = int(input(f"{input_color}Enter the delay time per request (seconds): {reset}"))

#     print(f"{info}Scraping members from {source_group.title}...{reset}")
#     participants = client(GetParticipantsRequest(
#         source_group,
#         filter=ChannelParticipantsSearch(''),
#         offset=0,
#         limit=scrape_limit,
#         hash=0
#     )).users

#     print(f"{success}Scraped {len(participants)} members. Adding them to {target_group.title}...{reset}")
#     for member in participants:
#         try:
#             client(InviteToChannelRequest(target_group, [member]))
#             print(f"{success}Added {member.username or member.id} to the target group!{reset}")
#             time.sleep(delay_time)
#         except UserAlreadyParticipantError:
#             print(f"{info}{member.username or member.id} is already in the group.{reset}")
#         except UserPrivacyRestrictedError:
#             print(f"{error}Cannot add {member.username or member.id}. Privacy settings restrict this.{reset}")
#         except Exception as e:
#             print(f"{error}Error adding {member.username or member.id}: {e}{reset}")

#     print(f"{info}All operations completed.{reset}")




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


# import os
# import uuid
# import platform
# from colorama import Fore

# # Define colors
# r = Fore.RED
# lg = Fore.GREEN
# rs = Fore.RESET
# cy = Fore.CYAN

# # File to store the unique device identifiers
# DEVICE_FILE = "device_ids.txt"
# MAX_DEVICES = 3

# def get_device_id():
#     """
#     Get a unique identifier for the device.
#     This example uses the MAC address, but you could use other unique identifiers like UUID.
#     """
#     if platform.system() in ["Linux", "Darwin"]:
#         # Get MAC address for Linux and macOS
#         mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 8*6, 8)][::-1])
#         return mac
#     elif platform.system() == "Windows":
#         # Get a unique machine ID on Windows
#         return str(uuid.getnode())  # MAC address or fallback to another unique ID
#     return str(uuid.getnode())  # Fallback to UUID if OS is unsupported

# def read_device_ids():
#     """
#     Read the stored device IDs from the device file.
#     """
#     if os.path.exists(DEVICE_FILE):
#         with open(DEVICE_FILE, "r") as file:
#             return file.read().splitlines()
#     return []

# def save_device_id(device_id):
#     """
#     Save the new device ID to the file.
#     """
#     with open(DEVICE_FILE, "a") as file:
#         file.write(device_id + "\n")

# def is_device_allowed():
#     """
#     Check if the device is allowed to run the script (i.e., not exceeding the device limit).
#     """
#     device_id = get_device_id()
#     device_ids = read_device_ids()

#     if device_id in device_ids:
#         print(f"{lg}Device already registered. Access granted.{rs}")
#         return True

#     if len(device_ids) >= MAX_DEVICES:
#         print(f"{r}Device limit reached ({MAX_DEVICES}). Cannot run the script on more devices.{rs}")
#         return False

#     save_device_id(device_id)
#     print(f"{lg}Device {device_id} registered successfully. Access granted.{rs}")
#     return True

# def main_three_devices():
#     if not is_device_allowed():
#         print(f"{r}Exiting... This device is not allowed to run the script.{rs}")
#         return False
#     print(f"{lg}Script is running...{rs}")
#     return True


import os
import uuid
import platform
import subprocess
from colorama import Fore

# Define colors
r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
cy = Fore.CYAN

# File to store the unique device identifiers
DEVICE_FILE = "device_ids.txt"
MAX_DEVICES = 3

def get_device_id():
    """
    Get a unique identifier for the device.
    This example uses the MAC address for desktops and the Android ID for Termux.
    """
    if platform.system() in ["Linux", "Darwin"]:
        if os.path.exists("/data/data/com.termux/files/usr/bin/termux-info"):
            # If running in Termux on Android, fetch the Android ID
            try:
                android_id = subprocess.check_output(
                    ["getprop", "ro.serialno"], universal_newlines=True
                ).strip()
                return android_id if android_id else str(uuid.getnode())
            except subprocess.SubprocessError:
                return str(uuid.getnode())
        else:
            # Get MAC address for Linux and macOS
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 8*6, 8)][::-1])
            return mac
    elif platform.system() == "Windows":
        # Get a unique machine ID on Windows
        return str(uuid.getnode())
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

    if device_id in device_ids:
        print(f"{lg}Device already registered. Access granted.{rs}")
        return True

    if len(device_ids) >= MAX_DEVICES:
        print(f"{r}Device limit reached ({MAX_DEVICES}). Cannot run the script on more devices.{rs}")
        return False

    save_device_id(device_id)
    print(f"{lg}Device {device_id} registered successfully. Access granted.{rs}")
    return True

def main_three_devices():
    if not is_device_allowed():
        print(f"{r}Exiting... This device is not allowed to run the script.{rs}")
        return False
    print(f"{lg}Script is running...{rs}")
    return True


import uuid
import os
import requests

# Function to get token from file
def get_token_from_file():
    try:
        with open('token.txt', 'r') as file:
            token = file.read().strip()  # Remove any extra whitespace or newline characters
            return token
    except FileNotFoundError:
        print("Error: token.txt file not found.")
        return None

# Function to generate or load a device ID
# def get_device_id():
#     device_id_file = 'device_ids.txt'

#     # If the device ID file exists, read the ID from it
#     if os.path.exists(device_id_file):
#         with open(device_id_file, 'r') as file:
#             device_id = file.read().strip()
#             return device_id
#     else:
#         # Generate a new device ID and save it to the file
#         device_id = str(uuid.uuid4())
#         with open(device_id_file, 'w') as file:
#             file.write(device_id)
#         return device_id

# Function to verify the device
# def verify_device():
#     device_id = get_device_id()
#     token = get_token_from_file()
#     if not token:
#         print("Error: Token not found.")
#         return False

#     verify_url = 'https://scrapeleet.com/accounts/verify-device/'

#     try:
#         response = requests.post(verify_url, data={'device_id': device_id, 'token': token})
#         response_data = response.json()

#         if response.status_code == 201:
#             print(f"Device with ID {device_id} verified successfully.")
#             return True
#         elif response.status_code == 400 and response_data.get("error") == "Device limit reached. Only 3 devices are allowed.":
#             print("Error: Device limit reached. Access denied.")
#             return False
#         elif response.status_code == 200:
#             print(f"Device already verified: {response_data.get('message')}")
#             return True
#         else:
#             print(f"Unexpected error: {response_data.get('error', response.text)}")
#             return False
#     except Exception as e:
#         print(f"An exception occurred: {e}")
#         return False


# Function to generate a unique device ID
import hashlib
import uuid
import platform

# def get_device_id():
#     # Fetch system-specific details
#     system_name = platform.node()  # Retrieves the system's hostname
#     mac_address = uuid.getnode()  # Retrieves the MAC address
#     system_info = f"{system_name}_{mac_address}"
    
#     # Hash the combined information for a consistent device ID
#     device_id = hashlib.sha256(system_info.encode()).hexdigest()
#     return device_id


# def verify_device(device_id, token):
#     verify_url = 'https://scrapeleet.com/accounts/verify-device/'
#     response = requests.post(verify_url, data={'device_id': device_id, 'token': token})
#     response_data = response.json()

#     if response.status_code == 201:
#         print("Device verified and registered successfully.")
#         return True
#     elif response.status_code == 400 and response_data.get("error") == "Device limit reached. Generate a new token to proceed.":
#         print("Error: Device limit reached. Please use a new token.")
#         return False
#     elif response.status_code == 200:
#         print(response_data.get("message"))
#         return True
#     else:
#         print(f"Unexpected error: {response_data.get('error', response.text)}")
#        return False

# Function to generate a unique and consistent device ID based on system details
import hashlib
import uuid
import platform
import subprocess

def get_device_id():
    unique_identifier = None

    try:
        if platform.system() == "Linux" and "termux" in platform.platform().lower():
            # Mobile device (Termux on Android)
            try:
                # Use `getprop` to retrieve the build fingerprint
                unique_identifier = subprocess.check_output(
                    "getprop ro.build.fingerprint", shell=True
                ).strip().decode()
            except subprocess.CalledProcessError:
                unique_identifier = None
            
            # Fallback to serial number if build fingerprint is unavailable
            if not unique_identifier:
                try:
                    unique_identifier = subprocess.check_output(
                        "getprop ro.serialno", shell=True
                    ).strip().decode()
                except subprocess.CalledProcessError:
                    unique_identifier = None

            # Fallback to Android ID if serial number is unavailable
            if not unique_identifier:
                try:
                    unique_identifier = subprocess.check_output(
                        "settings get secure android_id", shell=True
                    ).strip().decode()
                except subprocess.CalledProcessError:
                    unique_identifier = None

            # If no identifier is found, fallback to a default value
            if not unique_identifier or unique_identifier == "unknown":
                unique_identifier = "Fallback_Termux_Device"

        else:
            # For non-Termux systems, use uuid's node-based MAC address retrieval
            unique_identifier = uuid.getnode()
    except Exception as e:
        # Fallback if unique identifier retrieval fails
        unique_identifier = str(uuid.getnode())

    # Ensure unique_identifier is a string
    if isinstance(unique_identifier, int):
        unique_identifier = f"{unique_identifier:012x}"

    if not unique_identifier:
        unique_identifier = "UnknownIdentifier"

    # Generate the device ID based on the unique identifier
    device_id = hashlib.sha256(unique_identifier.encode()).hexdigest()
    return device_id



# Function to verify the device via the web app

import requests

def verify_device(device_id, token):
    verify_url = 'https://scrapeleet.com/accounts/verify-device/'
    response = requests.post(verify_url, data={'device_id': device_id, 'token': token})
    response_data = response.json()

    if response.status_code == 201:
        print("Device verified and registered successfully.")
        return True
    elif response.status_code == 200:
        print(response_data.get("message"))
        return True
    elif response.status_code == 403:  # Device limit reached
        print("Device limit reached. Only previously registered devices are allowed.")
        return True  # Allow access for already registered devices
    else:
        print(f"Error: {response_data.get('error', 'Unexpected error occurred.')}")
        return False




def main_menu():
    token = get_token_from_file()

    # Prompt for a valid token if none exists or if the token is invalid
    while True:
        if token is None:
            token = input(f"{lg}[+] Enter your purchase token or get it from https://scrapeleet.com: {rs}")
        else:
            is_valid, user_id = verify_token(token)
            if is_valid:
                print(f"{lg}[+] Loaded token verified for user ID: {user_id}. Access granted to the scraper.{rs}")
                save_token(token)
                break
            else:
                print(f"{r}[!] Invalid or expired token. Please enter a valid token or purchase one from https://scrapeleet.com.{rs}")
                token = input(f"{lg}[+] Enter your purchase token: {rs}")
                save_token(token)
                break

    # Check if the device is verified before allowing access to the main menu
    # if not verify_device():
    #     print(f"{r}[!] Device not verified. Exiting program.{rs}")
    #     return

    while True:
        device_id = get_device_id()

        if verify_device(device_id, token):
            print("Access granted.")
            # Main menu functionality goes here
            break
        else:
            print("Verification failed because devices limit reach 3. Try again with a new token.")

    # Retain the original menu style
    menu = f"""
{cy}╔════════════════════════════════════╗
{cy}║             {lg}Main Menu{cy}              ║
{cy}╚════════════════════════════════════╝

{lg}Account Management:

{lg}1.{rs} Manage Account
{lg}2.{rs} Set Your Profile Data and Photo

{lg}Automation - Scraping and Adding:

{lg}3.{rs} Automate Scraping and Members Adding
{lg}4.{rs} Scrape and Add Members (No Share Links)
{lg}5.{rs} Automate Scraping and Online Members Adding
{lg}6.{rs} Automate Scraping and Online Members Adding (No Share Links)
{lg}7.{rs} Automate Scraping and Hidden Members Adding
{lg}8.{rs} Automate Scraping and Hidden Members Adding (No Share Links)

{lg}Messaging:

{lg}9.{rs} Send Bulk Messages to All Scraped Members (DMs)
{lg}10.{rs} Moving New Messages From Group to Group
{lg}11.{rs} Moving New Messages From Group to Group (No Share Links)
{lg}12.{rs} Move Old Messages From Group to Group

{lg}Group Joining With Accounts:

{lg}13.{rs} Join Account to the choice group/channel
{lg}14.{rs} Remove Account from the choice group/channel

{lg}System:
{lg}15.{rs} Exit Scrapeleet
"""

    while True:
        print(menu)
        choice = input(f'\n{cy} Select an action: {rs}')

        if choice == '1':
            manager()
        elif choice == '2':
            print('Setting profile data is coming soon in the next update.')
        elif choice == '3':
            while True:
                automation()
        elif choice == '4':
            start_scraping_and_adding()
        elif choice == '5':
            automation_online_only()
        elif choice == '6':
            fetch_and_add_online_members()
        elif choice == '7':
            hidden_members()
        elif choice == '8':
            scrape_hidden_members_from_groups()
        elif choice == '9':
            scrape_and_send_bulk_message()
        elif choice == '10':
            move_messages()
        elif choice == '11':
            transfer_group_messages()
        elif choice == '12':
            move_old_messages()
        elif choice == '13':
            group_joiner()
        elif choice == '14':
            group_leaver()
        elif choice == '15':
            print('Thanks for using Scrapeleet!')
            break
        else:
            print(f"{r}Invalid choice! Please select a valid option.{rs}")
            continue

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{r}Operation interrupted by the user. Exiting...{rs}")