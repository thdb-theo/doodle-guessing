import JSON
using Plots

# function parse_drawing(s)

s = "{\"lines\":[{\"points\":[{\"x\":132.97976914327614,\"y\":310.42515808042566},{\"x\":132.97976914327614,\"y\":310.42515808042566},{\"x\":132.97976914327614,\"y\":310.42515808042566},{\"x\":132.97976914327614,\"y\":310.42515808042566},{\"x\":132.97976914327614,\"y\":310.42515808042566},{\"x\":132.97976914327614,\"y\":310.42515808042566},{\"x\":132.97976914327614,\"y\":310.42515808042566},{\"x\":132.98002229230661,\"y\":310.3079406945116},{\"x\":133.46248031623838,\"y\":306.21711834025666},{\"x\":134.47194033863124,\"y\":301.06195598961267},{\"x\":136.11871173859694,\"y\":295.7218256406785},{\"x\":140.29874696506732,\"y\":287.009163950727},{\"x\":142.53018666134932,\"y\":282.1174576712031},{\"x\":145.3862222616768,\"y\":276.0507374972987},{\"x\":147.3148331111382,\"y\":272.0168681649903},{\"x\":149.54171757403344,\"y\":267.1227110194712},{\"x\":151.06606348060342,\"y\":263.34774388488864},{\"x\":151.39208797239712,\"y\":262.47439644972445},{\"x\":153.0611664012078,\"y\":258.3457652862634},{\"x\":154.20913353839262,\"y\":255.40454812937477},{\"x\":155.64689765947097,\"y\":252.1700153718473},{\"x\":156.88637862743403,\"y\":249.80238328649537},{\"x\":157.91796207935755,\"y\":247.81886330350162},{\"x\":159.3002626361004,\"y\":245.47631148573944},{\"x\":160.0883032868854,\"y\":243.90589165255702},{\"x\":161.4168020796581,\"y\":241.0650858176793},{\"x\":162.37143943999,\"y\":239.04376699100743},{\"x\":162.98274263700117,\"y\":237.8523272090587},{\"x\":163.63579042310806,\"y\":236.66773771726423},{\"x\":164.03579059496016,\"y\":235.8793940271209},{\"x\":164.2812223278167,\"y\":235.46505460088835},{\"x\":165.00985372446655,\"y\":234.29986748556885},{\"x\":165.43694356401286,\"y\":233.55586460878092},{\"x\":165.72671293430483,\"y\":233.11774651525116},{\"x\":166.51493702982043,\"y\":231.9747129753896},{\"x\":167.32579809176048,\"y\":230.84182619117496},{\"x\":167.70691377689252,\"y\":230.37067947095906},{\"x\":167.70691377689252,\"y\":230.37067947095906},{\"x\":167.70691377689252,\"y\":230.37067947095906},{\"x\":167.70691377689252,\"y\":230.37067947095906},{\"x\":167.70691377689252,\"y\":230.37067947095906},{\"x\":167.70691377689252,\"y\":230.37067947095906},{\"x\":167.70691377689252,\"y\":230.37067947095906},{\"x\":167.70691377689252,\"y\":230.37067947095906},{\"x\":168.57360718433264,\"y\":230.67934719511834},{\"x\":173.86300351600198,\"y\":234.03568341037186},{\"x\":175.84788388020678,\"y\":235.68174517806193},{\"x\":178.18822366276092,\"y\":238.28747173294025},{\"x\":180.49484990674623,\"y\":241.0204906060672},{\"x\":184.09125138981733,\"y\":246.8655840408378},{\"x\":186.46559409229565,\"y\":250.27542160564357},{\"x\":189.03455851554574,\"y\":255.33717358540446},{\"x\":190.67005786335497,\"y\":259.03565880327704},{\"x\":192.23016491475025,\"y\":262.23992550610944},{\"x\":195.93482319189872,\"y\":269.38832540943145},{\"x\":198.0818837937875,\"y\":272.8713531702029},{\"x\":199.99630509753086,\"y\":275.92455873387223},{\"x\":201.15301123132633,\"y\":277.8278171771693},{\"x\":203.142062672459,\"y\":280.50803229354096},{\"x\":204.87037303547774,\"y\":282.7151653018682},{\"x\":207.0415571617109,\"y\":285.583363991352},{\"x\":208.32437346988326,\"y\":287.3751360043941},{\"x\":209.5709179687102,\"y\":289.20283754542163},{\"x\":210.37580424061915,\"y\":290.3384999797668},{\"x\":212.05918303735376,\"y\":292.5700446507123},{\"x\":213.33976907815287,\"y\":294.3641302281344},{\"x\":214.58431043078772,\"y\":296.1937155436823},{\"x\":216.2273745533631,\"y\":298.4452495542474},{\"x\":217.4864734970639,\"y\":300.26091266900903},{\"x\":218.30036969534507,\"y\":301.39236213429626},{\"x\":218.7532484968202,\"y\":302.08069125701036},{\"x\":219.0978414901592,\"y\":302.54099337446075},{\"x\":219.55698594631335,\"y\":303.2123526320895},{\"x\":219.55698594631335,\"y\":303.2123526320895}],\"brushColor\":\"#663399\",\"brushRadius\":10},{\"points\":[{\"x\":179.66775869618863,\"y\":235.8939100540587},{\"x\":179.66775869618863,\"y\":235.8939100540587},{\"x\":179.66775869618863,\"y\":235.8939100540587},{\"x\":178.11917033010218,\"y\":234.59413362536768},{\"x\":174.47497736550358,\"y\":230.2351263129262},{\"x\":171.6906444484025,\"y\":225.49170298502096},{\"x\":170.22709427982383,\"y\":222.7514011697484},{\"x\":168.26087535177135,\"y\":218.21800307904587},{\"x\":166.31622902828235,\"y\":212.5852999813431},{\"x\":165.5478671492456,\"y\":209.8246176719909},{\"x\":164.2847869064392,\"y\":204.89492337042358},{\"x\":163.39967149147512,\"y\":200.08959082493536},{\"x\":162.74850958017248,\"y\":195.19278977789173},{\"x\":162.20701477672853,\"y\":189.25345106037557},{\"x\":161.79243169178872,\"y\":182.28467431329892},{\"x\":161.54766678327778,\"y\":176.2969566989702},{\"x\":161.39961722204797,\"y\":171.3021766648073},{\"x\":161.2774277244432,\"y\":165.30523232338734},{\"x\":161.21490093583802,\"y\":161.30635815538346},{\"x\":161.1582091772817,\"y\":156.3071228155119},{\"x\":161.13049193240394,\"y\":153.30740802628537},{\"x\":161.1021293275049,\"y\":149.3076396211783},{\"x\":160.75917573513271,\"y\":143.28661065182177},{\"x\":160.58477333645564,\"y\":139.2953875715014},{\"x\":160.14825804510238,\"y\":134.25867561239932},{\"x\":159.85444260060487,\"y\":132.1782662523527},{\"x\":159.4276514593664,\"y\":128.2314654242858},{\"x\":159.09346878523556,\"y\":126.14227348995797},{\"x\":158.82173736712343,\"y\":124.18284348046207},{\"x\":158.28403254046094,\"y\":121.1103592108494},{\"x\":158.12586191870668,\"y\":120.1370506551446},{\"x\":157.63722733996735,\"y\":116.20710671366197},{\"x\":157.42416159848364,\"y\":114.23184233434966},{\"x\":157.2387052106128,\"y\":112.25052329042293},{\"x\":157.15239907176084,\"y\":111.25831606631347},{\"x\":157.0721068360345,\"y\":110.26505335844783},{\"x\":156.99741753912903,\"y\":109.27087772156575},{\"x\":156.99741753912903,\"y\":109.27087772156575}],\"brushColor\":\"#663399\",\"brushRadius\":10},{\"points\":[{\"x\":156.99741753912903,\"y\":109.27087772156575},{\"x\":156.99741753912903,\"y\":109.27087772156575},{\"x\":156.99741753912903,\"y\":109.27087772156575},{\"x\":156.99741753912903,\"y\":109.27087772156575},{\"x\":156.99741753912903,\"y\":109.27087772156575},{\"x\":156.99741753912903,\"y\":109.27087772156575},{\"x\":159.84320916493022,\"y\":109.06418441759683},{\"x\":163.89342145022795,\"y\":108.6026096487348},{\"x\":167.85857678062456,\"y\":108.25633818072038},{\"x\":169.9392812594006,\"y\":107.96128004744423},{\"x\":171.9072399042087,\"y\":107.71924838886149},{\"x\":174.00155439277353,\"y\":107.35710477360674},{\"x\":177.07233692192963,\"y\":106.73379009543513},{\"x\":179.18107681413326,\"y\":106.22188528158229},{\"x\":182.23303178914625,\"y\":105.42861294053597},{\"x\":183.41351295357518,\"y\":105.05835872179432},{\"x\":185.2670062589713,\"y\":104.55667948517356},{\"x\":188.53464449797633,\"y\":103.42563218328128},{\"x\":190.6182890677465,\"y\":102.66010756268331},{\"x\":191.81516101187222,\"y\":102.16383595311608},{\"x\":193.0119422593449,\"y\":101.61450351379413},{\"x\":195.35449251614716,\"y\":99.90101296113578},{\"x\":197.5695262476413,\"y\":98.1867839287728},{\"x\":200.53861902913164,\"y\":95.30366584368892},{\"x\":202.4102944170707,\"y\":93.12347708014106},{\"x\":203.76997298452244,\"y\":91.42136982654092},{\"x\":206.1897895390241,\"y\":87.41039529748234},{\"x\":207.32793201997282,\"y\":85.02312196553237},{\"x\":208.8995088597954,\"y\":81.27916316198355},{\"x\":209.53169913298754,\"y\":79.52561975938721},{\"x\":210.32767463260836,\"y\":76.78437895534744},{\"x\":210.91343171702158,\"y\":73.14064444555859},{\"x\":210.93483169850637,\"y\":69.30776574144063},{\"x\":210.10401250409592,\"y\":64.14058256503868},{\"x\":209.6707883997629,\"y\":62.03671382060604},{\"x\":207.79149051284418,\"y\":55.754283490345294},{\"x\":206.85623170352102,\"y\":53.38558465983986},{\"x\":204.7410223873276,\"y\":48.998241782087405},{\"x\":203.09191478853322,\"y\":45.82259593864368},{\"x\":202.06590406452673,\"y\":43.83606664266646},{\"x\":200.34383645723838,\"y\":40.688294821472326},{\"x\":198.9135031668397,\"y\":38.35792001198137},{\"x\":196.542462336705,\"y\":34.94678413482748},{\"x\":194.38128207865122,\"y\":32.31272618801183},{\"x\":193.93761260567814,\"y\":31.829672964110955},{\"x\":191.825932943957,\"y\":29.93172324899731},{\"x\":190.15921746844643,\"y\":28.54619047222649},{\"x\":188.43309758294046,\"y\":27.20540234192803},{\"x\":187.77781663515648,\"y\":26.74095656190792},{\"x\":187.08331151254032,\"y\":26.290534420511616},{\"x\":186.62509592099138,\"y\":25.951983458390792},{\"x\":184.07849463425305,\"y\":24.297956107262042},{\"x\":182.5740178133485,\"y\":23.470320710195445},{\"x\":180.61003079580857,\"y\":22.404412965975162},{\"x\":178.98727758849824,\"y\":21.653203890989836},{\"x\":176.38747335922184,\"y\":20.690738970925274},{\"x\":173.65881448034102,\"y\":19.87762655966289},{\"x\":169.88270219723543,\"y\":19.02270773422651},{\"x\":168.92653876667174,\"y\":18.821833448923183},{\"x\":166.1326787768381,\"y\":18.521023771142318},{\"x\":164.1512916504848,\"y\":18.335902335926928},{\"x\":161.1705060555941,\"y\":18.109162979306166},{\"x\":159.20852990840982,\"y\":18.10900876066266},{\"x\":157.1801147329947,\"y\":18.242318663391988},{\"x\":155.1098447722614,\"y\":18.496900130530495},{\"x\":153.13404718196438,\"y\":18.707686429396713},{\"x\":151.04539778499594,\"y\":19.039136465037906},{\"x\":148.94192900493826,\"y\":19.468427856419257},{\"x\":147.53247636785738,\"y\":19.937747397753753},{\"x\":144.27511607648344,\"y\":21.232433752748573},{\"x\":141.89965300569952,\"y\":22.377247571840293},{\"x\":138.72386607761777,\"y\":24.025956702156407},{\"x\":136.73723110430373,\"y\":25.05177023239935},{\"x\":135.16224443364197,\"y\":26.048604763023267},{\"x\":132.87963386430792,\"y\":27.62070860757265},{\"x\":131.74642982391595,\"y\":28.430894424228015},{\"x\":130.19350651022788,\"y\":29.711170957014396},{\"x\":129.11520228844552,\"y\":30.617083369929162},
{\"x\":128.6308727567662,\"y\":31.071903410529174},{\"x\":128.14388008060013,\"y\":31.579834946456565},{\"x\":126.7242569940316,\"y\":33.194540672877},{\"x\":125.3930835751467,\"y\":35.16683911684611},{\"x\":124.55063122842817,\"y\":36.643202782849215},{\"x\":123.44812125534324,\"y\":39.08088297926844},{\"x\":122.51579852430932,\"y\":41.11172189242534},{\"x\":121.3055540285644,\"y\":44.62696205129322},{\"x\":120.53894522391491,\"y\":47.38884490376537},{\"x\":120.0872594536617,\"y\":49.2720282798114},{\"x\":119.38299265126739,\"y\":53.12329048409361},{\"x\":118.94805705112007,\"y\":56.051239553505205},{\"x\":118.59147989077334,\"y\":59.00322868612348},{\"x\":118.22491961298614,\"y\":62.9641360188669},{\"x\":118.06538226699097,\"y\":64.95034716095456},{\"x\":117.92665957627253,\"y\":66.93994001679201},{\"x\":117.80607375465064,\"y\":68.93208674385924},{\"x\":117.83244896862699,\"y\":70.9091453670331},{\"x\":117.85561592597776,\"y\":72.90885663996363},{\"x\":117.86638387439804,\"y\":73.90873628449368},{\"x\":118.27805963721768,\"y\":77.02189152472715},{\"x\":118.39901413557538,\"y\":78.00646489175493},{\"x\":118.93994171286849,\"y\":80.2695999728723},{\"x\":119.28521542095636,\"y\":81.44396950917896},{\"x\":119.90885359627872,\"y\":82.93286086062344},{\"x\":120.54004186577356,\"y\":84.68731805405591},{\"x\":121.27735059361598,\"y\":86.21706735583639},{\"x\":122.58915533000349,\"y\":88.574036878915},{\"x\":123.64814914882236,\"y\":90.15056245401082},{\"x\":125.36473621170111,\"y\":92.13175736436257},{\"x\":126.29602103392415,\"y\":93.19171176862581},{\"x\":127.76305802930267,\"y\":94.68665165420714},{\"x\":129.9560642676614,\"y\":96.5529757485733},{\"x\":131.24452345898484,\"y\":97.46754070672975},{\"x\":133.07755600477097,\"y\":98.70838860626506},{\"x\":133.79081570609247,\"y\":99.1507518379451},{\"x\":135.6996722786387,\"y\":100.29990595880649},{\"x\":138.0889356984936,\"y\":101.43670261441623},{\"x\":138.92177054300657,\"y\":101.80228918752785},{\"x\":141.55612836895523,\"y\":102.72873500651819},{\"x\":142.45685747688242,\"y\":103.02195444117315},{\"x\":143.1380270766113,\"y\":103.17707188835085},{\"x\":143.1380270766113,\"y\":103.17707188835085}],\"brushColor\":\"#663399\",\"brushRadius\":10},{\"points\":[{\"x\":109.98402782904829,\"y\":175.53211122412063},{\"x\":109.98402782904829,\"y\":175.53211122412063},{\"x\":109.98402782904829,\"y\":175.53211122412063},{\"x\":109.98402782904829,\"y\":175.53211122412063},{\"x\":109.98402782904829,\"y\":175.53211122412063},{\"x\":109.98402782904829,\"y\":175.53211122412063},{\"x\":109.98402782904829,\"y\":175.53211122412063},{\"x\":109.98402782904829,\"y\":175.53211122412063},{\"x\":111.97706022287058,\"y\":175.21054384932648},{\"x\":115.90798101513674,\"y\":174.72526296341812},{\"x\":117.88359109291041,\"y\":174.51367211344453},{\"x\":120.95302480138754,\"y\":174.0557392369574},{\"x\":123.90460402619055,\"y\":173.69766941931508},{\"x\":126.97596725574577,\"y\":173.20375854986716},{\"x\":130.9073348004693,\"y\":172.7200198025989},{\"x\":132.02932496548726,\"y\":172.51218685788322},{\"x\":135.93890148612093,\"y\":171.95859996806104},{\"x\":141.870251900252,\"y\":171.38298686963296},{\"x\":145.92331424559796,\"y\":170.8449642918633},{\"x\":149.97471299858077,\"y\":170.19594406219946},{\"x\":151.93402459298633,\"y\":169.92382490936927},{\"x\":155.9844503989692,\"y\":169.2558461586948},{\"x\":159.91235087001166,\"y\":168.7602752109293},{\"x\":162.98416362891,\"y\":168.25410654615567},{\"x\":164.94117138913867,\"y\":167.97456040529408},{\"x\":167.89671209690906,\"y\":167.63120711023026},{\"x\":170.96748298327918,\"y\":167.15030051064005},{\"x\":172.92855781214897,\"y\":166.88401846887302},{\"x\":174.89913649658635,\"y\":166.65193309483357},{\"x\":176.0179956879438,\"y\":166.4501997442547},{\"x\":176.98971338899165,\"y\":166.28751939561707},{\"x\":177.96522859856796,\"y\":166.1358530650481},{\"x\":178.94403676774482,\"y\":165.99451113020478},{\"x\":179.9256990313193,\"y\":165.86283591941506},{\"x\":180.90983400050663,\"y\":165.740202637074},{\"x\":180.90983400050663,\"y\":165.740202637074},{\"x\":181.89611049271937,\"y\":165.6260196272949},{\"x\":183.98803346221678,\"y\":165.27746104762875},{\"x\":184.96377444659456,\"y\":165.12647779157416},{\"x\":186.92575394853517,\"y\":164.86324528848098},{\"x\":187.90988150839863,\"y\":164.74058384381559},{\"x\":189.88502666668796,\"y\":164.52701194368709},{\"x\":191.9742162822232,\"y\":164.19284102968487},{\"x\":192.95181512136762,\"y\":164.04761366598302},{\"x\":193.93242937256105,\"y\":163.912301744613},{\"x\":194.91565648293744,\"y\":163.78626778070415},{\"x\":195.90114679235782,\"y\":163.6689073954978},{\"x\":196.88859679884968,\"y\":163.55964925180186},{\"x\":198.0031186085754,\"y\":163.3661321370245},{\"x\":198.97683305252858,\"y\":163.20913539334012},{\"x\":199.95407992005377,\"y\":163.0627984113282},{\"x\":199.95407992005377,\"y\":163.0627984113282}],\"brushColor\":\"#663399\",\"brushRadius\":10}],\"width\":400,\"height\":400}"
d = JSON.parse(s)

lines = get(d, "lines", undef)

Xs = []
Ys = []
for line in lines
    xs = []
    ys = []
    for point in get(line, "points", undef)
        push!(xs, get(point, "x", undef))
        push!(ys, get(point, "y", undef))
    end
    push!(Xs, xs)
    push!(Ys, ys)
end
plot(Xs, Ys)
    # return xs, ys
# end
