API = float(input("\n Enter the API gravity : "))
GOR = float(input("\n Enter the Gas Oil Ratio : "))
Bo = float(input("\n Enter the Formation Oil Volume Factor : "))


if API < 35.0 and GOR < 200.0 and Bo <1.2:
  print(f"\n Low Shrinkage Crude, with: \nAPI:{API} Deg. \t GOR:{GOR} SCF/STB \t Bo:{Bo} RB/STB")
elif 35 <= API <=45 and 200<=GOR<=700 and 1.2<=Bo<=1.5:
  print(f"\n Ordinary Black Oil, with: \nAPI:{API} Deg. \t GOR:{GOR} SCF/STB \t Bo:{Bo} RB/STB")
elif 45==3000 and Bo >2:
  print(f"\n Near Critical Crude Oil, with: \nAPI:{API} Deg. \t GOR:{GOR} SCF/STB \t Bo:{Bo} RB/STB")
else:
  print("\n The entered properties don't fit into anny classification!")



API = float(input("\n Enter the API gravity : "))
GOR = float(input("\n Enter the Gas Oil Ratio : "))

if API > 50.0 and 8000 <=GOR<= 70000:
    print(f"\n Retrograde gas-condensate reservoir, with: \nAPI:{API} Deg. \t GOR:{GOR} SCF/STB \t")
elif API > 60.0 and 60000 <=GOR<=100000:
    print(f"\n Wet-gas reservoir, with: \nAPI:{API} Deg. \t GOR:{GOR} SCF/STB \t")