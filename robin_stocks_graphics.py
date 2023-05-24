import robin_stocks.robinhood as robin
from robin_stocks import*
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import matplotlib as mpl
import datetime

# function for retreiving RoobinHood un and pw to keep it hidden in source code
with open("RHcreds.txt", 'r') as file:
    data = file.read().replace('\n', '')

username, password = data.split(':')

# retrieved credentials from .txt file
robin.login(username,password)
    
def asset_class_compare_sctr_plt():
    my_stocks = robin.build_holdings()

    data = my_stocks
    #price = data['VOO']['price']
    #print(price)  

    VOO = 'VOO'
    pct_chg_voo = float(data[VOO]['percent_change'])
    equ_chg_voo = float(data[VOO]['equity_change'])
    avg_buy_price_voo = float(data[VOO]['average_buy_price'])
    quantity_ownd_voo = float(data[VOO]['quantity'])
    initial_princ_voo = avg_buy_price_voo * quantity_ownd_voo

    BRKB = 'BRK.B'
    pct_chg_brkb = float(data[BRKB]['percent_change'])
    equ_chg_brkb = float(data[BRKB]['equity_change'])
    avg_buy_price_brkb = float(data[BRKB]['average_buy_price'])
    quantity_ownd_brkb = float(data[BRKB]['quantity'])
    initial_princ_brkb = avg_buy_price_brkb * quantity_ownd_brkb

    tot_safe_pct_chg = round((pct_chg_voo + pct_chg_brkb),2)
    tot_safe_equ_chg = round((equ_chg_voo + equ_chg_brkb),2)
    tot_safe_princpl = round((initial_princ_voo + initial_princ_brkb),2)

    print(f'tot safe principl: ${tot_safe_princpl}')
    #print(f'tot safe % change: {tot_safe_pct_chg}')
    #print(f'tot safe $ change: {tot_safe_equ_chg}')

    spc_ass_list = []
    pct_chg_list = []
    pct_equ_list = []
    avg_buy_list = []
    qnt_own_list = []
    avgXown_list = []

    for key in my_stocks:
        if key == 'VOO' or key == 'BRK.B':
            continue # skip 'safe' stocks
        #print(key)
        spc_ass_list.append(key)
    for i in spc_ass_list:
        #print(i)
        pct_chg = float(my_stocks[i]['percent_change'])
        pct_chg_list.append(pct_chg)
        equ_chg = float(my_stocks[i]['equity_change'])
        pct_equ_list.append(equ_chg)
        avg_buy = float(my_stocks[i]['average_buy_price'])
        avg_buy_list.append(avg_buy)
        qnt_own = float(my_stocks[i]['quantity'])
        qnt_own_list.append(qnt_own)
        #print(f"Pct Change: {pct_chg}, Equity Change: {equ_chg}")
    pct_chg_sum = round((sum(pct_chg_list)/100),2)
    equ_chg_sum = round((sum(pct_equ_list)),2)
    for i in range(len(avg_buy_list)):
        product = avg_buy_list[i] * qnt_own_list[i]
        avgXown_list.append(product)
    #print(pct_chg_list)
    #print(pct_equ_list)
    #print(avg_buy_list)
    #print(qnt_own_list)
    #print(f'tot spec % change: {pct_chg_sum}')
    #print(f'tot spec $ change: {equ_chg_sum}')
    #print(f'tot spec $ avg pc: {avg_buy_sum}')
    #print(f'tot spec $ qnt wn: {qnt_own_sum}')
    avgXown_sum = round((sum(avgXown_list)),2)
    print(f'tot spec principl: ${avgXown_sum}')

### Principal Function #########

### BTC  Function ##############    
    btc_investment_amount = 9.95
    btc_quantity = 0.0004191
    btc_historical = robin.crypto.get_crypto_historicals('BTC', interval='hour', span='day')

    # Get the percent change for the BTC-USD pair on the day
    #percent_change = ((float(btc_historical[-1]['close_price']) / float(btc_historical[0]['open_price'])) - 1) * 100
    #print(f"The percent change for BTC today is {percent_change}%")

    btc_total_return = (btc_quantity * float(btc_historical[-1]['close_price'])) - btc_investment_amount
    #print(f"BTC total $ return: {btc_total_return:.2f}")

    btc_percent_return = ((btc_total_return /btc_investment_amount) * 100)
    #print(f"BTC total % return: {btc_percent_return:.2f}")

### ETH Function ################
    eth_investment_amount = 131.02
    eth_quantity = 0.069455
    eth_historical = robin.crypto.get_crypto_historicals('ETH', interval='hour', span='day')   

    # Get the percent change for the ETH-USD pair on the day
    #percent_change = ((float(eth_historical[-1]['close_price']) / float(eth_historical[0]['open_price'])) - 1) * 100
    #print(f"The percent change for ETH today is {percent_change}%")

    eth_total_return = (eth_quantity * float(eth_historical[-1]['close_price'])) - eth_investment_amount
    #print(f"ETH total $ return: {eth_total_return:.2f}")

    eth_percent_return = ((eth_total_return /eth_investment_amount) * 100)
    #print(f"ETH total % return: {eth_percent_return:.2f}") 

### AVAX Function ################
    avax_investment_amount = 10
    avax_quantity = 0.543
    avax_historical = robin.crypto.get_crypto_historicals('AVAX', interval='hour', span='day')   

    # Get the percent change for the ETH-USD pair on the day
    #percent_change = ((float(eth_historical[-1]['close_price']) / float(eth_historical[0]['open_price'])) - 1) * 100
    #print(f"The percent change for ETH today is {percent_change}%")

    avax_total_return = (avax_quantity * float(avax_historical[-1]['close_price'])) - avax_investment_amount
    #print(f"AVAX total $ return: {avax_total_return:.2f}")

    avax_percent_return = ((avax_total_return /avax_investment_amount) * 100)
    #print(f"AVAX total % return: {avax_percent_return:.2f}") 

    ### LTC  Function ##############    
    ltc_investment_amount = 20
    ltc_quantity = 0.09669076
    ltc_historical = robin.crypto.get_crypto_historicals('LTC', interval='hour', span='day')

    # Get the percent change for the BTC-USD pair on the day
    #percent_change = ((float(btc_historical[-1]['close_price']) / float(btc_historical[0]['open_price'])) - 1) * 100
    #print(f"The percent change for BTC today is {percent_change}%")

    ltc_total_return = (ltc_quantity * float(ltc_historical[-1]['close_price'])) - ltc_investment_amount
    #print(f"LTC total $ return: {ltc_total_return:.2f}")

    ltc_percent_return = ((ltc_total_return /ltc_investment_amount) * 100)
    #print(f"LTC total % return: {ltc_percent_return:.2f}")

    ### SHIB  Function ##############    
    shib_investment_amount = 25
    shib_quantity = 1194457.00
    shib_historical = robin.crypto.get_crypto_historicals('SHIB', interval='hour', span='day')

    # Get the percent change for the BTC-USD pair on the day
    #percent_change = ((float(btc_historical[-1]['close_price']) / float(btc_historical[0]['open_price'])) - 1) * 100
    #print(f"The percent change for BTC today is {percent_change}%")

    shib_total_return = (shib_quantity * float(shib_historical[-1]['close_price'])) - shib_investment_amount
    #print(f"SHIB total $ return: {shib_total_return:.2f}")

    shib_percent_return = ((shib_total_return /shib_investment_amount) * 100)
    #print(f"SHIB total % return: {shib_percent_return:.2f}")

    total_crypto_pct_rtn = round(((btc_percent_return/100) + (eth_percent_return/100) + (avax_percent_return/100) + (ltc_percent_return/100) + (shib_percent_return/100)),2)
    #print(f"tot cryp % change: {total_crypto_pct_rtn:.2f}")

    total_crypto_equ_rtn = round((sum([btc_total_return, eth_total_return, avax_total_return, ltc_total_return, shib_total_return])),2)
    #print(f"tot cryp $ change: {total_crypto_equ_rtn:.2f}")

### Sum of Total Crypto Initial Investment ###
    crypto_principal_list = [btc_investment_amount, eth_investment_amount, avax_investment_amount,
                             ltc_investment_amount, shib_investment_amount]
    crypto_principal_totl = round(sum(crypto_principal_list),2)
    print(f'tot cryp principl: ${crypto_principal_totl}')

############# Main Logic for Data Frame and Data Storage ####################
    today = datetime.datetime.now().date()
    today_str = str(today)
    #print(today_str)
    
    df = pd.read_csv('daily_asset_class_data.csv')

    last_date_val = df['Date'].iloc[-1]
    last_date_val_str = str(last_date_val)
    #print(last_date_val_str)

    if last_date_val_str != today_str:

        new_data = {'Date': [today], 
                    'VOO&BRK%': [tot_safe_pct_chg], 'VOO&BRK$': [tot_safe_equ_chg], 
                    'EstvWld%': [pct_chg_sum],      'EstvWld$': [equ_chg_sum], 
                    'Cryptic%': [total_crypto_pct_rtn], 'Cryptic$':[total_crypto_equ_rtn]}
        
        new_df = pd.DataFrame(new_data)
        print(new_df)

        df = pd.concat([df, new_df], ignore_index=True)
        print(df)

        df.to_csv('daily_asset_class_data.csv', index=False)

    else:
        print("Asset data has already been collected today.")

        df = pd.read_csv('daily_asset_class_data.csv')

        # Set 'Date' as the index of the DataFrame
        df = df.set_index('Date')

        df_pct = df.iloc[:, 1::2]
        #print(df_pct)

        df_equ = df.iloc[:, ::2]
        #print(df_equ)

        df_now = df.iloc[-1]
        print(df_now)

        # Create a subplots plot of the DataFrames
        fig, (ax1, ax2, ax3) = plt.subplots(3)

        # Add title and axis labels
        fig.suptitle("eBot's Asset Comparision", 
                     fontsize=15, x=.5, y=.94, fontweight='bold', ha='center')
        
        ax1.set_xlabel('Date')
        ax1.set_ylabel('$ Change')
        ax1.set_title('')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('% Change')
        ax2.set_title('')
        ax3.set_xlabel('')
        ax3.set_ylabel('Total Change')
        ax3.set_title('')
        
        # Create scatter plots with lines connecting the points
        df_pct.plot(ax=ax1, marker = 'o', linestyle = '-')
        df_equ.plot(ax=ax2, marker = 'o', linestyle = '-')
        df_now.plot.bar(ax=ax3, color = ['blue', 'blue', 'orange', 'orange', 'green', 'green'])      

        # Add total values to the top of the bars
        for i, v in enumerate(df_now):
            ax3.text(i, v, str(v), color='grey', ha='center')


        # Adjust subplot spacing
        plt.subplots_adjust(hspace=0.4)

        # Show the plot
        #plt.show()

    # Principle amounts by class data
    labels1 = ['VOO&BRK', 'EstvWld', 'Cryptic']
    sizes1 = [tot_safe_princpl, avgXown_sum, crypto_principal_totl]
    colors = ['blue', 'orange', 'green']
    # ROI amounts by class data
    labels2 = ['VOO&BRK', 'EstvWld', 'Cryptic']
    # if statement to change color if value becomes negative
    if total_crypto_equ_rtn <= 0:
        total_crypto_equ_rtn = abs(total_crypto_equ_rtn)
        crypt_color = 'red'
    else: crypt_color = 'green'
    sizes2 = [tot_safe_equ_chg, equ_chg_sum, total_crypto_equ_rtn]
    colors = ['blue', 'orange', crypt_color]

    fig = plt.gcf()

    # create custom label string
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return '{p:.1f}%\n(${v:d})'.format(p=pct, v=val)
        return my_autopct
    
    ax4 = fig.add_axes([0.1, 0.1, 0.35, 0.35])
    # create pie chart with custom labels
    ax4.pie(sizes1, labels=labels1, colors=colors, autopct=make_autopct(sizes1))
    ax4.set_title('AST Distribution')

    # create second pie chart
    ax5 = fig.add_axes([0.1, 0.1, 0.75, 0.75])
    ax5.pie(sizes2, labels=labels2, colors=colors, autopct=make_autopct(sizes2))
    ax5.set_title('ROI Distribution')

    # adjust layout and display plot
    plt.tight_layout()
    plt.show()

asset_class_compare_sctr_plt()