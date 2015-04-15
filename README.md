# CERN-alias

# setup

The script ```setup.sh``` sets up a local user area on LXPLUS and installs various programs to this user area. The programs it installs are as follows:

- ranger
- Irssi

Run the script in the following way:

```Bash
source setup.sh
```

# icons

The colours of icons can be changed using a command such as the following (which would change the colour from CERN blue to grey:

```Bash
sed -i 's/#3861aa/#666666/g' *
```
