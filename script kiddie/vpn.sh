#!/bin/bash
#usage takes in a parameter
#use list
if [ $# -eq 0 ]
	then 
		echo "Usage: $(basename $0) ... (atleast 1 argument)" 1>&2
exit 1
fi
#smart
if [ $1 = "smart" ]
	then
		expressvpn connect smart
fi
#hongkong
if [ $1 = "hk2" ] || [ $1 = "hk" ]
	then
		expressvpn connect hk2
elif [ $1 = "hong" ] && [ $2 = "kong" ]
   then
      expressvpn connect hk2
fi

#losangeles
if [ $1 = "usla" ] || [ $1 = "la" ]
	then
		expressvpn connect usla
elif [ $1 = "los" ] && [ $2 = "angeles" ]
   then
      expressvpn connect usla
elif [ $1 = "usla2" ] || [ $1 = "la2" ]
   then
      expressvpn connect usla2
elif [ $1 = "usla3" ] || [ $1 = "la3" ]
   then
      expressvpn connect usla3
fi


#newyork
if [ $1 = "usny" ] || [ $1 = "ny" ]
	then
		expressvpn connect usny
elif [ $1 = "new" ] && [ $2 = "york" ]
   then
      expressvpn connect usny
fi

#washingtonDC
if [ $1 = "uswd" ] || [ $1 = "washington" ] 
	then
		expressvpn connect uswd
elif [ $1 = "dc" ]
   then
      expressvpn connect uswd
fi
#dallas
if [ $1 = "usda" ] || [ $1 = "dallas" ] 
	then
		expressvpn connect usda
fi
#sanfrancisco
if [ $1 = "ussf" ] || [ $1 = "sf" ] 
	then
		expressvpn connect ussf
elif [ $1 = "san" ] && [ $2 = "fran" ] 
   then
      expressvpn connect ussf
elif [ $1 = "san" ] && [ $2 = "francisco" ] 
   then
      expressvpn connect ussf
fi

#seattle
if [ $1 = "usse" ] || [ $1 = "seattle" ] 
	then
		expressvpn connect usse
fi
#chicago
if [ $1 = "usch" ] || [ $1 = "chicago" ] 
	then
		expressvpn connect usch
fi
#miami
if [ $1 = "usmi" ] || [ $1 = "miami" ] 
	then
		expressvpn connect usmi
elif [ $1 = "florida" ]
   then
      expressvpn connect usmi
fi
#newjersery
if [ $1 = "usnj1" ] || [ $1 = "nj" ] 
	then
		expressvpn connect usnj1
elif [ $1 = "new" ] && [ $2 = "jersey" ]
      then 
         expressvpn connect usnj1
fi
#denver
if [ $1 = "usde" ] || [ $1 = "denver" ] 
	then
		expressvpn connect usde
fi
#salt lake city
if [ $1 = "ussl1" ] 
	then
		expressvpn connect ussl1
elif [ $1 = "salt" ] && [ $2 = "lake" ] && [ $3 = "city" ] 
   then
      expressvpn connect ussl1 
fi
#tampa
if [ $1 = "tampa" ]
   then
      expressvpn connect usta1
fi

#holly wood
if [ $1 = "usho" ] 
	then
		expressvpn connect usho
elif [ $1 = "holly" ] && [ $2 = "wood" ] 
   then
      expressvpn connect usho

fi

#atlanta
if [ $1 = "usat" ] || [ $1 = "atlanta" ] 
	then
		expressvpn connect usat
fi
#santa monica
if [ $1 = "ussm" ] 
	then
		expressvpn connect ussm
elif [ $1 = "santa" ] && [ $2 = "monica" ] 
   then
    expressvpn connect ussm
fi

#japan (tokyo)
if [ $1 = "jpto" ]
   then
      expressvpn connect jpto
elif [ $1 = "jpto2" ]
   then
      expressvpn connect jpt02
elif [ $1 = "jpyo" ]
   then
      expressvpn connect jpyo 
elif [ $1 = "japan" ]
   then
      echo "1. tokyo"
      echo "2. tokyo server 2"
      echo "3. yokohama"
      read input
if [ $input -eq 1 ]
   then
      expressvpn connect jpto
fi
if [ $input -eq 2 ]
   then
      expressvpn connect jpto2
fi
if [ $input -eq 3 ]
   then
      expressvpn connect jpyo
fi
fi

#australia (melbourne)
if [ $1 = "aume" ]
   then
      expressvpn connect aume
#australia (sydeny)
elif [ $1 = "ausy" ]
   then
      expressvpn connect ausy
#australia (sydeny) server 2
elif [ $1 = "ausy2" ]
   then
      expressvpn connect ausy2
#australia (perth)
elif [ $1 = "aupe" ]
   then
      expressvpn connect aume
#australia (brisbane)
elif [ $1 = "aubr" ]
   then
      expressvpn connect aubr
#australia
elif [ $1 = "australia" ]
   then 
      echo "1. melbourne"
      echo "2. sydney"
      echo "3. sydney server 2"
      echo "4. perth"
      echo "5. brisbane"
         read input
if [ $input -eq 1 ]
   then
      expressvpn connect aume
fi
if [ $input -eq 2 ]
   then
      expressvpn connect ausy
fi
if [ $input -eq 3 ]
   then
      expressvpn connect ausy2
fi
if [ $input -eq 4 ]
   then 
      expressvpn connect aupe
fi
if [ $input -eq 5 ]
   then
      expressvpn connect aubr
fi
fi

#malaysia
if [ $1 = "my" ] || [ $1 = "malaysia" ]
   then 
      expressvpn connect my
fi
#sri lanka
if [ $1 = "lk" ] 
   then 
      expressvpn connect lk
#sri lanka cont
elif [ $1 = "sri" ] && [ $2 = "lanka" ]
   then 
      expressvpn connect lk
fi 
#pakistan
if [ $1 = "pk" ] || [ $1 = "pakistan" ]
   then 
      expressvpn connect pk
fi
#kazakhstan
if [ $1 = "ks" ] || [ $1 = "kazakhstan" ]
   then 
      expressvpn connect my
fi
#thailand
if [ $1 = "th" ] || [ $1 = "thailand" ]
   then 
      expressvpn connect th
fi
#indonesia
if [ $1 = "id" ] || [ $1 = "indonesia" ]
   then 
      expressvpn connect id
fi
#new zealand
if [ $1 = "nz" ] 
   then 
      expressvpn connect nz
elif [ $1 = "new" ] && [ $2 = "zealand" ]
   then 
      expressvpn connect nz
fi

#taiwan
if [ $1 = "tw3" ] || [ $1 = "taiwan" ]
   then 
      expressvpn connect tw3
fi
#vietnam
if [ $1 = "vn" ] || [ $1 = "vietnam" ]
   then 
      expressvpn connect vn
fi
#macau
if [ $1 = "mo" ] || [ $1 = "macau" ]
   then 
      expressvpn connect mo
fi
#cambodia
if [ $1 = "kh" ] || [ $1 = "cambodia" ]
   then 
      expressvpn connect kh
fi
#mongolia
if [ $1 = "mn" ] || [ $1 = "mongolia" ]
   then 
      expressvpn connect mn
fi
#laos
if [ $1 = "laos" ] 
   then 
      expressvpn connect la
fi
#nepal
if [ $1 = "np" ] || [ $1 = "nepal" ] 
   then 
      expressvpn connect np
fi
#kyrgyzstan
if [ $1 = "kg" ] || [ $1 = "kyrgyzstan" ] 
   then 
      expressvpn connect kg
fi
#uzbekistan
if [ $1 = "uz" ] || [ $1 = "uzbekistan" ] 
   then 
      expressvpn connect uz
fi
#bangladesh
if [ $1 = "bd" ] || [ $1 = "bangladesh" ] 
   then 
      expressvpn connect bd
fi
#bhutan
if [ $1 = "bt" ] || [ $1 = "bhutan" ] 
   then 
      expressvpn connect bt
fi
#brunei
if [ $1 = "bnbr" ] || [ $1 = "brunei" ] 
   then 
      expressvpn connect bnbr
fi
#mexico
if [ $1 = "mx" ] || [ $1 = "mexico" ] 
   then 
      expressvpn connect mx
fi
#brazil
if [ $1 = "br" ] || [ $1 = "brazil" ] 
   then 
      expressvpn connect br
fi
#panama
if [ $1 = "pa" ] || [ $1 = "panama" ] 
   then 
      expressvpn connect pa
fi
#chile
if [ $1 = "cl" ] || [ $1 = "chile" ] 
   then 
      expressvpn connect cl
fi
#argentina
if [ $1 = "ar" ] || [ $1 = "argentina" ] 
   then 
      expressvpn connect ar
fi
#bolivia
if [ $1 = "bo" ] || [ $1 = "bolivia" ] 
   then 
      expressvpn connect bo
fi
#costa rica
if [ $1 = "cr" ]
   then 
      expressvpn connect cr
elif [ $1 = "costa" ] && [ $2 = "rica" ]
   then
      expressvpn connect cr
fi
#costa rica cont

#columbia
if [ $1 = "co" ] || [ $1 = "columbia" ]  
   then 
      expressvpn connect co
fi
#venezuela
if [ $1 = "ve" ] || [ $1 = "venezuela" ]  
   then 
      expressvpn connect ve
fi
#ecuador
if [ $1 = "ec" ] || [ $1 = "ecuador" ]  
   then 
      expressvpn connect ec
fi
#guatemala
if [ $1 = "gt" ] || [ $1 = "guatemala" ]  
   then 
      expressvpn connect gt
fi
#peru
if [ $1 = "pe" ] || [ $1 = "peru" ]  
   then 
      expressvpn connect pe
fi
#uruguay
if [ $1 = "uy" ] || [ $1 = "uruguay" ]  
   then 
      expressvpn connect uy
fi
#bahamas
if [ $1 = "bs" ] || [ $1 = "bahamas" ]  
   then 
      expressvpn connect bs
fi
#sweden (has server2)
if [ $1 = "se" ] || [ $1 = "sweden" ]  
   then 
      expressvpn connect se
fi
#romania
if [ $1 = "ro" ] || [ $1 = "romania" ]  
   then 
      expressvpn connect ro
fi
#isle of man
if [ $1 = "im" ]  
   then 
      expressvpn connect im
fi
#isle of man
if [ $1 = "isle" ] && [ $2 = "of" ] && [ $3 = "man" ]  
   then 
      expressvpn connect im
fi
#turkey
if [ $1 = "tr" ] || [ $1 = "turkey" ]  
   then 
      expressvpn connect tr
fi
#ireland
if [ $1 = "ie" ] || [ $1 = "ireland" ]  
   then 
      expressvpn connect ie
fi
#iceland
if [ $1 = "is" ] || [ $1 = "iceland" ]  
   then 
      expressvpn connect tr
fi
#norway
if [ $1 = "no" ] || [ $1 = "norway" ]  
   then 
      expressvpn connect no
fi
#denmark
if [ $1 = "dk" ] || [ $1 = "denmark" ]  
   then 
      expressvpn connect dk
fi
#belgium
if [ $1 = "be" ] || [ $1 = "belgium" ]  
   then 
      expressvpn connect be
fi
#finland
if [ $1 = "fi" ] || [ $1 = "finland" ]  
   then 
      expressvpn connect fi
fi
#greece
if [ $1 = "gr" ] || [ $1 = "greece" ]  
   then 
      expressvpn connect gr
fi
#portugal
if [ $1 = "pt" ] || [ $1 = "portugal" ]  
   then 
      expressvpn connect pt
fi
#austria
if [ $1 = "at" ] || [ $1 = "austria" ]  
   then 
      expressvpn connect at
fi
#armenia
if [ $1 = "am" ] || [ $1 = "armenia" ]  
   then 
      expressvpn connect am
fi
#poland
if [ $1 = "pl" ] || [ $1 = "poland" ]  
   then 
      expressvpn connect pl
fi
#lithuania
if [ $1 = "lt" ] || [ $1 = "lithuania" ]  
   then 
      expressvpn connect lt
fi
#lativa
if [ $1 = "lv" ] || [ $1 = "lativa" ]  
   then 
      expressvpn connect lv
fi
#estonia
if [ $1 = "ee" ] ||[ $1 = "estonia" ]  
   then 
      expressvpn connect ee
fi
#czech republic
if [ $1 = "cz" ]   
   then 
      expressvpn connect cz
elif [ $1 = "czech" ] && [ $2 = "republic" ]  
   then 
      expressvpn connect cz
fi

#andorra
if [ $1 = "ad" ] || [ $1 = "andorra" ]  
   then 
      expressvpn connect ad
fi

#montenegro
if [ $1 = "me" ] || [ $1 = "montenegro" ]  
   then 
      expressvpn connect me
fi

#bosnia and hezegovina
if [ $1 = "ba" ]  
   then 
      expressvpn connect ba
elif [ $1 = "bosnia" ] && [ $2 = "and" ] && [ $3 = "hezegovina" ]  
   then 
      expressvpn connect ba
fi

#luxembourg
if [ $1 = "lu" ] || [ $1 = "luxembourg" ]  
   then 
      expressvpn connect lu
fi
#hungary
if [ $1 = "hu" ] || [ $1 = "hungary" ]  
   then 
      expressvpn connect hu
fi
#bulgaria
if [ $1 = "bg" ] || [ $1 = "bulgaria" ]  
   then 
      expressvpn connect bg
fi
#belarus
if [ $1 = "by" ] || [ $1 = "belarus" ]  
   then 
      expressvpn connect by
fi
#ukraine
if [ $1 = "ua" ] || [ $1 = "ukraine" ]  
   then 
      expressvpn connect ua
fi
#malta
if [ $1 = "mt" ] || [ $1 = "malta" ]  
   then 
      expressvpn connect mt
fi
#liechtenstein
if [ $1 = "li" ] || [ $1 = "liechtenstein" ]  
   then 
      expressvpn connect li
fi
#cyprus
if [ $1 = "cy" ] || [ $1 = "cyprus" ]  
   then 
      expressvpn connect cy
fi
#albania
if [ $1 = "al" ] || [ $1 = "albania" ]  
   then 
      expressvpn connect al
fi
#croatia
if [ $1 = "hr" ] || [ $1 = "croatia" ]  
   then 
      expressvpn connect hr
fi
#slovenia
if [ $1 = "si" ] || [ $1 = "slovenia" ]  
   then 
      expressvpn connect si
fi
#slovakia
if [ $1 = "sk" ] || [ $1 = "slovakia" ]  
   then 
      expressvpn connect sk
fi
#monaco
if [ $1 = "mc" ] || [ $1 = "monaco" ]  
   then 
      expressvpn connect mc
fi
#jersey
if [ $1 = "je" ] || [ $1 = "jersey" ]  
   then 
      expressvpn connect je
fi
#north macedonia
if [ $1 = "mk" ]  
   then 
      expressvpn connect mk
elif [ $1 = "north" ] && [ $2 = "macedonia" ]
   then
      expressvpn connect mk
fi

#moldova
if [ $1 = "md" ] || [ $1 = "moldova" ]
   then 
      expressvpn connect md
fi

#serbia
if [ $1 = "rs" ] || [ $1 = "serbia" ]
   then 
      expressvpn connect rs
fi

#georgia
if [ $1 = "ge" ] || [ $1 = "georgia" ]
   then 
      expressvpn connect ge
fi

#south africa
if [ $1 = "za" ] 
   then 
      expressvpn connect za
elif [ $1 = "south" ] && [ $2 = "africa" ]
   then 
      expressvpn connect za
fi

#israel
if [ $1 = "il" ] || [ $1 = "israel" ] 
   then 
      expressvpn connect il
fi

#egypt
if [ $1 = "eg" ] || [ $1 = "egypt" ] 
   then 
      expressvpn connect eg
fi

#south korea
if [ $1 = "kr2" ] || [ $1 = "korea" ]  
   then 
      expressvpn connect kr2
elif [ $1 = "south" ] && [ $2 = "korea" ]  
   then 
      expressvpn connect kr2
fi

#philippines
if [ $1 = "ph" ] ||  [ $1 = "pi" ] || [ $1 = "philippines" ]
   then 
      expressvpn connect ph
fi

#algeria
if [ $1 = "dz" ] || [ $1 = "algeria" ]
   then
      expressvpn connect dz
fi




############################
#singapore (jurong)
if [ $1 = "sgju" ] || [ $1 = "singapore" ]
	then
		expressvpn connect sgju
fi
#india
if [ $1 = "in" ] || [ $1 = "india" ]
	then
		expressvpn connect in
fi
#canadatoronto
if [ $1 = "cato" ]
	then
		expressvpn connect cato
elif [ $1 = "camo" ]
   then
      expressvpn connect camo
elif [ $1 = "canada" ]
   then
      echo "1. toronto"
      echo "2. montreal"
      read input
      if [ $input -eq 1 ]
         then
            expressvpn connect cato
      elif [ $input -eq 2 ]
         then 
            expressvpn connect camo
      fi
fi





#germanyfrankfurt
if [ $1 = "defr1" ] || [ $1 = "germany" ]
	then
		expressvpn connect defr1
fi
#ukdocklands
if [ $1 = "ukdo" ]
	then
		expressvpn connect ukdo
#uklondon
elif [ $1 = "uklo" ]
   then
      expressvpn connect uklo
elif [ $1 = "uk" ] || [ $1 = "united kindom" ]
   then
      echo "choose 1 for docklands"
      echo "choose 2 for london"
      read input
      if [ $input -eq 1 ] 
         then
            expressvpn connect ukdo
      fi
      if [ $input -eq 2 ]
         then
            expressvpn connect uklo
      fi
fi

#netherlands
if [ $1 = "nlam" ] || [ $1 = "netherlands" ]
	then
		expressvpn connect nlam
fi
#spainbarcelona
if [ $1 = "esba2" ] || [ $1 = "spain" ] || [ $1 = "barcelona" ]
	then
		expressvpn connect esba2
fi
#switzerland
if [ $1 = "ch2" ] || [ $1 = "switzerland" ]
	then
		expressvpn connect ch2
fi
#france
if [ $1 = "frpa1" ] || [ $1 = "france" ]
	then
		expressvpn connect frpa1
fi
#italy
if [ $1 = "itmi" ] || [ $1 = "italy" ]
	then
		expressvpn connect itmi
fi
#list
if [ $1 = "-l" ]
	then
		expressvpn list
fi
#list all
if [ $1 = "-la" ]
	then
		expressvpn list all
fi
#disconnect
if [ $1 = "-d" ] || [ $1 = "disconnect" ] 
	then
		expressvpn disconnect
fi
#status
if [ $1 = "-s" ] || [ $1 = "status" ] || [ $1 = "-status" ]
	then
		expressvpn status
fi

#preferences
if [ $1 = "p" ] || [ $1 = "preferences" ] || [ $1 = "-p" ] 
	then
		expressvpn preferences
fi

#blocking trackers 
if [ $1 = "block" ] || [ $1 = "-b" ] || [ $1 = "-block" ] || [ $1 = "--block" ] && [ $2 = "t" ] || [ $2 = "T" ] || [ $2 = "True" ] || [ $2 = "true" ]  
	then
		expressvpn preferences set block_trackers true; expressvpn disconnect; expressvpn connect smart
elif [ $1 = "block" ] || [ $1 = "-b" ] || [ $1 = "-block" ] || [ $1 = "--block" ]  && [ $2 = "f" ] || [ $2 = "F" ] || [ $2 = "False" ] || [ $2 = "false" ]  
	then
		expressvpn preferences set block_trackers false; expressvpn disconnect; expressvpn connect smart 
fi

#version
if [ $1 = "-v" ] || [ $1 = "-V" ] || [ $1 = "--version" ] || [ $1 = "-version" ] || [ $1 = "-Version" ] || [ $1 = "--Version" ] 
	then expressvpn --version
fi

#help
if [ $1 = "-h" ] || [ $1 = "-help" ]
   then
      expressvpn help
fi
#protocol
#lightway
if [ $1 = "protocol" ] || [ $1 = "-protocol" ] && [ $2 = "lightway_udp" ] || [ $2 = "-lightway_udp" ]
   then
      expressvpn protocol lightway_udp
#status
elif [ $2 = "-status" ] || [ $2 = "status" ] || [ $2 = "-s" ]
   then
      expressvpn protocol
#auto
elif [ $2 = "auto" ] || [ $2 = "-auto" ] || [ $2 = "-a" ]
   then
      expressvpn protocol auto
#lightway
elif [ $2 = "-lightway_tcp" ] || [ $2 = "lightway_tcp"]
   then  
      expressvpn protocol lightway_tcp
#openvpn
elif [ $2 = "tcp" ] || [ $2 = "-tcp" ]
   then
      expressvpn protocol tcp
elif [ $2 = "udp" ] || [ $2 = "-udp" ]
   then
      expressvpn protocol udp
fi