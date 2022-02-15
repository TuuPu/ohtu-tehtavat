*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Pekka
    Set Password  Topohanta123
    Set Password Confirmation  Topohanta123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Pe
    Set Password  Topohanta123
    Set Password Confirmation  Topohanta123
    Submit Register Credentials
    Register Should Fail With Message  Username too short or includes a character not allowed

Register With Valid Username And Too Short Password
    Set Username  Kukkuu
    Set Password  Topo1
    Set Password Confirmation  Topo1
    Submit Register Credentials
    Register Should Fail With Message  Password too short or only includes alphabets

Register With Nonmatching Password And Password Confirmation
    Set Username  Kuukkeli
    Set Password  Topohanta1
    Set Password Confirmation  Topohanta212121
    Submit Register Credentials
    Register Should Fail With Message  Password and confirmation do not match

*** Keywords ***
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Register Page
    Go To Register Page
    Register Page Should Be Open