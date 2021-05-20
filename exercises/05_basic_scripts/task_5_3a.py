# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""
modes = {
"access": ['Введите номер VLAN:'],
"trunk": ['Введите разрешенные VLANы']
}

requests = {
"access": [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
],

"trunk": [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
}

mode = input('Введите режим работы интерфейса (access/trunk): ')
type_num = input('Введите тип и номер интерфейса: ')
vlans = input('{}'.format(modes[mode]))
print('interface {}'.format(type_num))
print('\n'.join(requests[mode]).format(vlans))

