## Бодлого зохиогч нарын анхааралд!

Бүх флагны формат адилхан байх ёстой ба флаг формат нь **MUSTCTF{}** байна. 

- Бодлогоо оруулахдаа тус тусын category-д оруулах ба дараах зарчмыг баримтална. Үүнд: 

    Тухайн бодлогыг зохих category-д оруулах ба тухайн category-д бодлого тус бүрийн нэртэй folder байх ба тухайн folder-т заавал "challenge" folder болон "challenge.yml" файл байна. "challenge" folder-т тухайн бодлогонд хэрэглэгдэх ( upload хийгдэх ) файлаа байршуулах ба "challenge.yml" файл дараах бүтэцтэй байна.

    name: 

      - **YOUR CHALLENGE NAME**

    author: 

      - **YOUR NAME**

    category: 

      - **CATEGORY**
        **CATEGORY MUST BE ONE OF crypto/forensics/misc/osint/programming/pwn/reverse/web**

    description:

                   |-
      **DESCRIPTION**

    value: 

      **ENTER VALUE OF YOUR PROBLEM**

    type:  

      **standart/dynamic**

      - If it's dynamic -> :

        - extra:

          initial: 1000 **ENTER INITIAL POINT OF YOUR PROBLEM**
          decay: 50 **DECREASING POINTS FROM SECOND SOLVER**
          minimum: 500 **ENTER THE MINIMUM SCORE FOR YOUR PROBLEM**

    flags:

      **ADD FLAG OF YOUR PROBLEM, THAT MUST BE STARTS WITH "MUSTCTF{}"**

    files:
    
      - challenge/**PATH OF YOUR FILE**

Ойлгоход туслах, санаа авах байдлаар /round1/Cryptography дотор **color** даалгаврыг орууллаа. Challenge folder, "challenge.yml" болон "README.md" файлтай заавал уншиж танилцана уу.