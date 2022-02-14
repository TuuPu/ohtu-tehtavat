*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  koikkeli  kallekalle222
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  testi123
    Output Should Contain  Username already in use

Register With Too Short Username And Valid Password
    Input Credentials  ku  kukkuu2222
    Output Should Contain  Username too short or includes a character not allowed

Register With Valid Username And Too Short Password
    Input Credentials  kukkuu  k1
    Output Should Contain  Password too short or only includes alphabets

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kukkuu  tarpeeksipitkasalasanailmanerikoismerkkeja
    Output Should Contain  Password too short or only includes alphabets

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command