def sort_reindeer(reindeer_names):
    for i, j in enumerate(reindeer_names):
        print(i, j.split()[-1])


print(sort_reindeer(['Kenjiro Mori', 'Susumu Tokugawa', 'Juzo Okita', 'Akira Sanada']),
      ['Kenjiro Mori', 'Juzo Okita', 'Akira Sanada', 'Susumu Tokugawa'])
print(sort_reindeer([]), [])
print(sort_reindeer(
    ['Yasuo Kodai', 'Kenjiro Sado', 'Daisuke Aihara', 'Susumu Shima', 'Akira Sanada', 'Yoshikazu Okita',
     'Shiro Yabu', 'Sukeharu Nanbu', 'Sakezo Yamamoto', 'Hikozaemon Ohta', 'Juzo Mori', 'Saburo Tokugawa']),
    ['Daisuke Aihara', 'Yasuo Kodai', 'Juzo Mori', 'Sukeharu Nanbu', 'Hikozaemon Ohta',
     'Yoshikazu Okita', 'Kenjiro Sado', 'Akira Sanada', 'Susumu Shima', 'Saburo Tokugawa',
     'Shiro Yabu', 'Sakezo Yamamoto'])
print(
    sort_reindeer(['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto']),
    ['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])
print(
    sort_reindeer(["Sukeharu Yamamoto", "Juzo Yabu", "Saburo Shima", "Shiro Sanada", "Daisuke Mori"]),
    ['Daisuke Mori', 'Shiro Sanada', 'Saburo Shima', 'Juzo Yabu', 'Sukeharu Yamamoto'])
