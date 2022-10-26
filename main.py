name: 'H-W'

on:
  #push:
  schedule:
    # UTC (国内 UTC+8)
     - cron: '03 10 * * *'
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  H:
    runs-on: macos-12
    env:
      HOMEBREW_NO_INSTALL_CLEANUP: 1

    steps:
        - name: 'Checkout codes'
          uses: actions/checkout@v2
          
        - name: ' Environment Settings'
          run: |
            brew upgrade --cask google-chrome
            brew install ffmpeg
            pip3 install -r ./requirements.txt
            pip3 install undetected-chromedriver
            yes | pip3 uninstall selenium
            pip3 install selenium==4.2.0            
 
        - name: 'Renew-H'
          env:
            URL_BASE: ${{ secrets.URL_BASE_H }}
            USER_ID: ${{ secrets.USER_ID }}
            PASS_WD: ${{ secrets.PASS_WD }}
            BARK_KEY: ${{ secrets.BARK_KEY }}
            TG_BOT_TOKEN: ${{ secrets.TG_BOT_TOKEN }}
            TG_USER_ID: ${{ secrets.TG_USER_ID }}

          run: |
            python3 ./main.py
            
  W:
    runs-on: macos-12
    env:
      HOMEBREW_NO_INSTALL_CLEANUP: 1

    steps:
        - name: 'Checkout codes'
          uses: actions/checkout@v2
          
        - name: ' Environment Settings'
          run: |
            brew upgrade --cask google-chrome
            brew install ffmpeg
            pip3 install -r ./requirements.txt
            pip3 install undetected-chromedriver
            yes | pip3 uninstall selenium
            pip3 install selenium==4.2.0      
        - name: 'Renew-W'
          env:
            URL_BASE: ${{ secrets.URL_BASE_W }}
            USER_ID: ${{ secrets.USER_ID }}
            PASS_WD: ${{ secrets.PASS_WD }}
            BARK_KEY: ${{ secrets.BARK_KEY }}
            TG_BOT_TOKEN: ${{ secrets.TG_BOT_TOKEN }}
            TG_USER_ID: ${{ secrets.TG_USER_ID }}

          run: |
            python3 ./main.py
