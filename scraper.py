#!/usr/bin/env python
import scraperwiki
import urllib2
import lxml.etree

urls = ["http://www.finance.gov.au/sites/default/files/P35_BRODTMANN_Gai.pdf","http://www.finance.gov.au/sites/default/files/P35_HUMPHRIES_Gary.pdf","http://www.finance.gov.au/sites/default/files/P35_LEIGH_Andrew.pdf","http://www.finance.gov.au/sites/default/files/P35_LUNDY_Kate.pdf","http://www.finance.gov.au/sites/default/files/P35_SESELJA_Zed.pdf","http://www.finance.gov.au/sites/default/files/P35_ABBOTT_Tony.pdf","http://www.finance.gov.au/sites/default/files/P35_ALBANESE_Anthony.pdf","http://www.finance.gov.au/sites/default/files/P35_ALEXANDER_John.pdf","http://www.finance.gov.au/sites/default/files/P35_BALDWIN_Bob.pdf","http://www.finance.gov.au/sites/default/files/P35_BIRD_Sharon.pdf","http://www.finance.gov.au/sites/default/files/P35_BISHOP_Bronwyn.pdf","http://www.finance.gov.au/sites/default/files/P35_BOWEN_Chris.pdf","http://www.finance.gov.au/sites/default/files/P35_BURKE_Tony.pdf","http://www.finance.gov.au/sites/default/files/P35_CAMERON_Doug.pdf","http://www.finance.gov.au/sites/default/files/P35_CARR_Bob.pdf","http://www.finance.gov.au/sites/default/files/P35_CLARE_Jason.pdf","http://www.finance.gov.au/sites/default/files/P35_CLAYDON_Sharon.pdf","http://www.finance.gov.au/sites/default/files/P35_COBB_John.pdf","http://www.finance.gov.au/sites/default/files/P35_COLEMAN_David.pdf","http://www.finance.gov.au/sites/default/files/P35_COMBET_Greg.pdf","http://www.finance.gov.au/sites/default/files/P35_CONROY_Pat.pdf","http://www.finance.gov.au/sites/default/files/P35_COULTON_Mark.pdf","http://www.finance.gov.au/sites/default/files/P35_DASTYARI_Sam.pdf","http://www.finance.gov.au/sites/default/files/P35_ELLIOT_Justine.pdf","http://www.finance.gov.au/sites/default/files/P35_FAULKNER_John.pdf","http://www.finance.gov.au/sites/default/files/P35_FERGUSON_Laurie.pdf","http://www.finance.gov.au/sites/default/files/P35_FIERRAVANTI-WELLS_Concetta.pdf","http://www.finance.gov.au/sites/default/files/P35_FITZGIBBON_Joel.pdf","http://www.finance.gov.au/sites/default/files/P35_FLETCHER_Paul.pdf","http://www.finance.gov.au/sites/default/files/P35_GILLESPIE_David.pdf","http://www.finance.gov.au/sites/default/files/P35_GRIERSON_Sharon.pdf","http://www.finance.gov.au/sites/default/files/P35_HALL_Jill.pdf","http://www.finance.gov.au/sites/default/files/P35_HARTSUYKER_Luke.pdf","http://www.finance.gov.au/sites/default/files/P35_HAWKE_Alex.pdf","http://www.finance.gov.au/sites/default/files/P35_HAYES_Chris.pdf","http://www.finance.gov.au/sites/default/files/P35_HEFFERNAN_Bill.pdf","http://www.finance.gov.au/sites/default/files/P35_HENDY_Peter.pdf","http://www.finance.gov.au/sites/default/files/P35_HOCKEY_Joe.pdf","http://www.finance.gov.au/sites/default/files/P35_HOGAN_Kevin.pdf","http://www.finance.gov.au/sites/default/files/P35_HUSIC_Ed.pdf","http://www.finance.gov.au/sites/default/files/P35_JONES_Stephen.pdf","http://www.finance.gov.au/sites/default/files/P35_JOYCE_Barnaby1.pdf","http://www.finance.gov.au/sites/default/files/P35_KELLY_Craig.pdf","http://www.finance.gov.au/sites/default/files/P35_KELLY_Mike.pdf","http://www.finance.gov.au/sites/default/files/P35_LAUNDY_Craig.pdf","http://www.finance.gov.au/sites/default/files/P35_LEY_Sussan.pdf","http://www.finance.gov.au/sites/default/files/P35_LEYONHJELM_David.pdf","http://www.finance.gov.au/sites/default/files/P35_MARKUS_Louise.pdf","http://www.finance.gov.au/sites/default/files/P35_MATHESON_Russell.pdf","http://www.finance.gov.au/sites/default/files/P35_MCCORMACK_Michael.pdf","http://www.finance.gov.au/sites/default/files/P35_MCNAMARA_Karen.pdf","http://www.finance.gov.au/sites/default/files/P35_MORRISON_Scott.pdf","http://www.finance.gov.au/sites/default/files/P35_NASH_Fiona.pdf","http://www.finance.gov.au/sites/default/files/P35_O'NEILL_Deborah0.pdf","http://www.finance.gov.au/sites/default/files/P35_O'NEILL_Deborah1.pdf","http://www.finance.gov.au/sites/default/files/P35_OWENS_Julie.pdf","http://www.finance.gov.au/sites/default/files/P35_PAYNE_Marise.pdf","http://www.finance.gov.au/sites/default/files/P35_PLIBERSEK_Tanya.pdf","http://www.finance.gov.au/sites/default/files/P35_RHIANNON_Lee.pdf","http://www.finance.gov.au/sites/default/files/P35_ROWLAND_Michelle.pdf","http://www.finance.gov.au/sites/default/files/P35_RUDDOCK_Philip.pdf","http://www.finance.gov.au/sites/default/files/P35_SCOTT_Fiona.pdf","http://www.finance.gov.au/sites/default/files/P35_SINODINOS_Arthur.pdf","http://www.finance.gov.au/sites/default/files/P35_STEPHENS_Ursula.pdf","http://www.finance.gov.au/sites/default/files/P35_SUDMALIS_Ann.pdf","http://www.finance.gov.au/sites/default/files/P35_TAYLOR_Angus.pdf","http://www.finance.gov.au/sites/default/files/P35_THISTLETHWAITE_Matt0.pdf","http://www.finance.gov.au/sites/default/files/P35_THISTLETHWAITE_Matt1.pdf","http://www.finance.gov.au/sites/default/files/P35_TURNBULL_Malcolm.pdf","http://www.finance.gov.au/sites/default/files/P35_VARVARIS_Nickolas.pdf","http://www.finance.gov.au/sites/default/files/P35_WICKS_Lucy.pdf","http://www.finance.gov.au/sites/default/files/P35_WILLIAMS_John.pdf","http://www.finance.gov.au/sites/default/files/P35_CROSSIN_Trish.pdf","http://www.finance.gov.au/sites/default/files/P35_GRIGGS_Natasha.pdf","http://www.finance.gov.au/sites/default/files/P35_PERIS_Nova.pdf","http://www.finance.gov.au/sites/default/files/P35_SCULLION_Nigel.pdf","http://www.finance.gov.au/sites/default/files/P35_SNOWDON_Warren.pdf","http://www.finance.gov.au/sites/default/files/P35_ANDREWS_Karen.pdf","http://www.finance.gov.au/sites/default/files/P35_BOSWELL_Ronald.pdf","http://www.finance.gov.au/sites/default/files/P35_BOYCE_Sue.pdf","http://www.finance.gov.au/sites/default/files/P35_BRANDIS_George.pdf","http://www.finance.gov.au/sites/default/files/P35_BROUGH_Mal.pdf","http://www.finance.gov.au/sites/default/files/P35_BUCHHOLZ_Scott.pdf","http://www.finance.gov.au/sites/default/files/P35_BUTLER_Terri.pdf","http://www.finance.gov.au/sites/default/files/P35_CANAVAN_Matthew.pdf","http://www.finance.gov.au/sites/default/files/P35_CHALMERS_Jim.pdf","http://www.finance.gov.au/sites/default/files/P35_CHRISTENSEN_George.pdf","http://www.finance.gov.au/sites/default/files/P35_CIOBO_Steven.pdf","http://www.finance.gov.au/sites/default/files/P35_DUTTON_Peter.pdf","http://www.finance.gov.au/sites/default/files/P35_EMERSON_Craig.pdf","http://www.finance.gov.au/sites/default/files/P35_ENTSCH_Warren.pdf","http://www.finance.gov.au/sites/default/files/P35_FURNER_Mark.pdf","http://www.finance.gov.au/sites/default/files/P35_GAMBARO_Teresa.pdf","http://www.finance.gov.au/sites/default/files/P35_HOGG_John.pdf","http://www.finance.gov.au/sites/default/files/P35_HOWARTH_Luke.pdf","http://www.finance.gov.au/sites/default/files/P35_JONES_Ewen.pdf","http://www.finance.gov.au/sites/default/files/P35_JOYCE_Barnaby0.pdf","http://www.finance.gov.au/sites/default/files/P35_KATTER_Bob.pdf","http://www.finance.gov.au/sites/default/files/P35_KETTER_Chris.pdf","http://www.finance.gov.au/sites/default/files/P35_LAMING_Andrew.pdf","http://www.finance.gov.au/sites/default/files/P35_LANDRY_Michelle.pdf","http://www.finance.gov.au/sites/default/files/P35_LAZARUS_Glenn.pdf","http://www.finance.gov.au/sites/default/files/P35_LUDWIG_Joe.pdf","http://www.finance.gov.au/sites/default/files/P35_MACDONALD_Ian.pdf","http://www.finance.gov.au/sites/default/files/P35_MACFARLANE_Ian.pdf","http://www.finance.gov.au/sites/default/files/P35_MASON_Brett.pdf","http://www.finance.gov.au/sites/default/files/P35_MCGRATH_James.pdf","http://www.finance.gov.au/sites/default/files/P35_MCLUCAS_Jan.pdf","http://www.finance.gov.au/sites/default/files/P35_MOORE_Claire.pdf","http://www.finance.gov.au/sites/default/files/P35_NEUMANN_Shayne.pdf","http://www.finance.gov.au/sites/default/files/P35_NEVILLE_Paul.pdf","http://www.finance.gov.au/sites/default/files/P35_O'DOWD_Ken.pdf","http://www.finance.gov.au/sites/default/files/P35_O'SULLIVAN_Barry.pdf","http://www.finance.gov.au/sites/default/files/P35_PALMER_Clive.pdf","http://www.finance.gov.au/sites/default/files/P35_PERRETT_Graham.pdf","http://www.finance.gov.au/sites/default/files/P35_PITT_Keith.pdf","http://www.finance.gov.au/sites/default/files/P35_PRENTICE_Jane.pdf","http://www.finance.gov.au/sites/default/files/P35_RIPOLL_Bernie.pdf","http://www.finance.gov.au/sites/default/files/P35_ROBERT_Stuart.pdf","http://www.finance.gov.au/sites/default/files/P35_ROY_Wyatt.pdf","http://www.finance.gov.au/sites/default/files/P35_RUDD_Kevin.pdf","http://www.finance.gov.au/sites/default/files/P35_SCOTT_Bruce.pdf","http://www.finance.gov.au/sites/default/files/P35_SWAN_Wayne.pdf","http://www.finance.gov.au/sites/default/files/P35_TRUSS_Warren.pdf","http://www.finance.gov.au/sites/default/files/P35_VAN_MANEN_Bert.pdf","http://www.finance.gov.au/sites/default/files/P35_VASTA_Ross.pdf","http://www.finance.gov.au/sites/default/files/P35_WATERS_Larissa.pdf","http://www.finance.gov.au/sites/default/files/P35_BERNARDI_Cory.pdf","http://www.finance.gov.au/sites/default/files/P35_BIRMINGHAM_Simon.pdf","http://www.finance.gov.au/sites/default/files/P35_BRIGGS_Jamie.pdf","http://www.finance.gov.au/sites/default/files/P35_BUTLER_Mark.pdf","http://www.finance.gov.au/sites/default/files/P35_CHAMPION_Nick.pdf","http://www.finance.gov.au/sites/default/files/P35_DAY_Bob.pdf","http://www.finance.gov.au/sites/default/files/P35_EDWARDS_Sean.pdf","http://www.finance.gov.au/sites/default/files/P35_ELLIS_Kate.pdf","http://www.finance.gov.au/sites/default/files/P35_FARRELL_Don.pdf","http://www.finance.gov.au/sites/default/files/P35_FAWCETT_David.pdf","http://www.finance.gov.au/sites/default/files/P35_GALLACHER_Alex.pdf","http://www.finance.gov.au/sites/default/files/P35_HANSON-YOUNG_Sarah.pdf","http://www.finance.gov.au/sites/default/files/P35_MCEWEN_Anne.pdf","http://www.finance.gov.au/sites/default/files/P35_PASIN_Tony.pdf","http://www.finance.gov.au/sites/default/files/P35_PYNE_Christopher.pdf","http://www.finance.gov.au/sites/default/files/P35_RAMSEY_Rowan.pdf","http://www.finance.gov.au/sites/default/files/P35_RISHWORTH_Amanda.pdf","http://www.finance.gov.au/sites/default/files/P35_RUSTON_Anne.pdf","http://www.finance.gov.au/sites/default/files/P35_SOUTHCOTT_Andrew.pdf","http://www.finance.gov.au/sites/default/files/P35_WILLIAMS_Matt.pdf","http://www.finance.gov.au/sites/default/files/P35_WONG_Penny.pdf","http://www.finance.gov.au/sites/default/files/P35_WRIGHT_Penny.pdf","http://www.finance.gov.au/sites/default/files/P35_XENOPHON_Nick.pdf","http://www.finance.gov.au/sites/default/files/P35_ZAPPIA_Tony.pdf","http://www.finance.gov.au/sites/default/files/P35_ABETZ_Eric.pdf","http://www.finance.gov.au/sites/default/files/P35_BILYK_Catryna.pdf","http://www.finance.gov.au/sites/default/files/P35_BROWN_Carol.pdf","http://www.finance.gov.au/sites/default/files/P35_BUSHBY_David.pdf","http://www.finance.gov.au/sites/default/files/P35_COLBECK_Richard.pdf","http://www.finance.gov.au/sites/default/files/P35_COLLINS_Julie.pdf","http://www.finance.gov.au/sites/default/files/P35_HUTCHINSON_Eric.pdf","http://www.finance.gov.au/sites/default/files/P35_LAMBIE_Jacqui.pdf","http://www.finance.gov.au/sites/default/files/P35_MILNE_Christine.pdf","http://www.finance.gov.au/sites/default/files/P35_NIKOLIC_Andrew.pdf","http://www.finance.gov.au/sites/default/files/P35_PARRY_Stephen.pdf","http://www.finance.gov.au/sites/default/files/P35_POLLEY_Helen.pdf","http://www.finance.gov.au/sites/default/files/P35_SINGH_Lisa.pdf","http://www.finance.gov.au/sites/default/files/P35_THORP_Lin.pdf","http://www.finance.gov.au/sites/default/files/P35_URQUHART_Anne.pdf","http://www.finance.gov.au/sites/default/files/P35_WHISH-WILSON_Peter.pdf","http://www.finance.gov.au/sites/default/files/P35_WHITELEY_Brett.pdf","http://www.finance.gov.au/sites/default/files/P35_WILKIE_Andrew.pdf","http://www.finance.gov.au/sites/default/files/P35_ANDREWS_Kevin.pdf","http://www.finance.gov.au/sites/default/files/P35_BANDT_Adam.pdf","http://www.finance.gov.au/sites/default/files/P35_BILLSON_Bruce.pdf","http://www.finance.gov.au/sites/default/files/P35_BROAD_Andrew.pdf","http://www.finance.gov.au/sites/default/files/P35_BROADBENT_Russell.pdf","http://www.finance.gov.au/sites/default/files/P35_BURKE_Anna.pdf","http://www.finance.gov.au/sites/default/files/P35_BYRNE_Anthony.pdf","http://www.finance.gov.au/sites/default/files/P35_CARR_Kim.pdf","http://www.finance.gov.au/sites/default/files/P35_CHESTER_Darren.pdf","http://www.finance.gov.au/sites/default/files/P35_CHESTERS_Lisa.pdf","http://www.finance.gov.au/sites/default/files/P35_COLLINS_Jacinta.pdf","http://www.finance.gov.au/sites/default/files/P35_CONROY_Stephen.pdf","http://www.finance.gov.au/sites/default/files/P35_DANBY_Michael.pdf","http://www.finance.gov.au/sites/default/files/P35_DI_NATALE_Richard.pdf","http://www.finance.gov.au/sites/default/files/P35_DREYFUS_Mark.pdf","http://www.finance.gov.au/sites/default/files/P35_FEENEY_David.pdf","http://www.finance.gov.au/sites/default/files/P35_FIFIELD_Mitch.pdf","http://www.finance.gov.au/sites/default/files/P35_FORREST_John.pdf","http://www.finance.gov.au/sites/default/files/P35_FRYDENBERG_Josh.pdf","http://www.finance.gov.au/sites/default/files/P35_GILES_Andrew.pdf","http://www.finance.gov.au/sites/default/files/P35_GRIFFIN_Alan.pdf","http://www.finance.gov.au/sites/default/files/P35_HENDERSON_Sarah.pdf","http://www.finance.gov.au/sites/default/files/P35_HUNT_Greg.pdf","http://www.finance.gov.au/sites/default/files/P35_KING_Catherine.pdf","http://www.finance.gov.au/sites/default/files/P35_KROGER_Helen.pdf","http://www.finance.gov.au/sites/default/files/P35_MACKLIN_Jenny.pdf","http://www.finance.gov.au/sites/default/files/P35_MADIGAN_John.pdf","http://www.finance.gov.au/sites/default/files/P35_MARLES_Richard.pdf","http://www.finance.gov.au/sites/default/files/P35_MARSHALL_Gavin.pdf","http://www.finance.gov.au/sites/default/files/P35_MCGOWAN_Cathy.pdf","http://www.finance.gov.au/sites/default/files/P35_MCKENZIE_Bridget.pdf","http://www.finance.gov.au/sites/default/files/P35_MITCHELL_Rob.pdf","http://www.finance.gov.au/sites/default/files/P35_MUIR_Ricky.pdf","http://www.finance.gov.au/sites/default/files/P35_O'CONNOR_Brendan.pdf","http://www.finance.gov.au/sites/default/files/P35_O'DWYER_Kelly.pdf","http://www.finance.gov.au/sites/default/files/P35_O'NEIL_Clare.pdf","http://www.finance.gov.au/sites/default/files/P35_RICE_Janet.pdf","http://www.finance.gov.au/sites/default/files/P35_ROBB_Andrew.pdf","http://www.finance.gov.au/sites/default/files/P35_RONALDSON_Michael.pdf","http://www.finance.gov.au/sites/default/files/P35_ROXON_Nicola.pdf","http://www.finance.gov.au/sites/default/files/P35_RYAN_Joanne.pdf","http://www.finance.gov.au/sites/default/files/P35_RYAN_Scott.pdf","http://www.finance.gov.au/sites/default/files/P35_SHORTEN_Bill.pdf","http://www.finance.gov.au/sites/default/files/P35_SMITH_Tony.pdf","http://www.finance.gov.au/sites/default/files/P35_STONE_Sharman.pdf","http://www.finance.gov.au/sites/default/files/P35_SUKKAR_Michael.pdf","http://www.finance.gov.au/sites/default/files/P35_SYMON_Mike.pdf","http://www.finance.gov.au/sites/default/files/P35_TEHAN_Dan.pdf","http://www.finance.gov.au/sites/default/files/P35_THOMSON_Kelvin.pdf","http://www.finance.gov.au/sites/default/files/P35_TILLEM_Mehmet.pdf","http://www.finance.gov.au/sites/default/files/P35_TUDGE_Alan.pdf","http://www.finance.gov.au/sites/default/files/P35_VAMVAKINOU_Maria.pdf","http://www.finance.gov.au/sites/default/files/P35_WATTS_Tim.pdf","http://www.finance.gov.au/sites/default/files/P35_WOOD_Jason.pdf","http://www.finance.gov.au/sites/default/files/P35_BACK_Chris.pdf","http://www.finance.gov.au/sites/default/files/P35_BISHOP_Julie.pdf","http://www.finance.gov.au/sites/default/files/P35_BISHOP_Mark.pdf","http://www.finance.gov.au/sites/default/files/P35_BULLOCK_Joe.pdf","http://www.finance.gov.au/sites/default/files/P35_CASH_Michaelia.pdf","http://www.finance.gov.au/sites/default/files/P35_CORMANN_Mathias0.pdf","http://www.finance.gov.au/sites/default/files/P35_CORMANN_Mathias1.pdf","http://www.finance.gov.au/sites/default/files/P35_EGGLESTON_Alan.pdf","http://www.finance.gov.au/sites/default/files/P35_GOODENOUGH_Ian.pdf","http://www.finance.gov.au/sites/default/files/P35_GRAY_Gary.pdf","http://www.finance.gov.au/sites/default/files/P35_HAASE_Barry.pdf","http://www.finance.gov.au/sites/default/files/P35_IRONS_Steve.pdf","http://www.finance.gov.au/sites/default/files/P35_JENSEN_Dennis.pdf","http://www.finance.gov.au/sites/default/files/P35_JOHNSTON_David.pdf","http://www.finance.gov.au/sites/default/files/P35_KEENAN_Michael.pdf","http://www.finance.gov.au/sites/default/files/P35_LINES_Sue.pdf","http://www.finance.gov.au/sites/default/files/P35_LUDLAM_Scott.pdf","http://www.finance.gov.au/sites/default/files/P35_MACTIERNAN_Alannah.pdf","http://www.finance.gov.au/sites/default/files/P35_MARINO_Nola.pdf","http://www.finance.gov.au/sites/default/files/P35_PARKE_Melissa.pdf","http://www.finance.gov.au/sites/default/files/P35_PORTER_Christian.pdf","http://www.finance.gov.au/sites/default/files/P35_PRATT_Louise.pdf","http://www.finance.gov.au/sites/default/files/P35_PRICE_Melissa.pdf","http://www.finance.gov.au/sites/default/files/P35_RANDALL_Don.pdf","http://www.finance.gov.au/sites/default/files/P35_REYNOLDS_Linda.pdf","http://www.finance.gov.au/sites/default/files/P35_SIEWERT_Rachel.pdf","http://www.finance.gov.au/sites/default/files/P35_SIMPKINS_Luke.pdf","http://www.finance.gov.au/sites/default/files/P35_SMITH_Dean.pdf","http://www.finance.gov.au/sites/default/files/P35_STERLE_Glenn.pdf","http://www.finance.gov.au/sites/default/files/P35_WANG_Zhenya.pdf","http://www.finance.gov.au/sites/default/files/P35_WASHER_Mal.pdf","http://www.finance.gov.au/sites/default/files/P35_WILSON_Rick.pdf","http://www.finance.gov.au/sites/default/files/P35_WYATT_Ken.pdf"]
urls2 = ["http://www.finance.gov.au/sites/default/files/P35_BISHOP_Bronwyn.pdf"]

for url in urls:
    pdfdata = urllib2.urlopen(url).read()
    print "getting " + url
    print "The pdf file has %d bytes" % len(pdfdata)
    
    xmldata = scraperwiki.pdftoxml(pdfdata)
    
    #print "After converting to xml it has %d bytes" % len(pdfdata)
    #print "The first 2000 characters are: ", pdfdata
    #print xmldata
    parser = lxml.etree.XMLParser(recover=True)
    root = lxml.etree.XML(xmldata, parser)
    pages = list(root)
    
    #print "The pages are numbered:", [ page.attrib.get("number")  for page in pages ]
    
    # this function has to work recursively because we might have "<b>Part1 <i>part 2</i></b>"
    def gettext_with_bi_tags(el):
        res = [ ]
        if el.text:
            res.append(el.text)
        for lel in el:
            res.append("<%s>" % lel.tag)
            res.append(gettext_with_bi_tags(lel))
            res.append("</%s>" % lel.tag)
            if el.tail:
                res.append(el.tail)
        return "".join(res)
    
    #Get politician's name
    
    politician = url.split('/')[-1].split('.pdf')[0].replace('_', ' ')
    print politician
    
    
    # check through the PDF to find the travel expense pages, store in list
    
    travelExpPg = [] 

    for pageno, page in enumerate(pages):
        for el in list(page):
            #print el.attrib, gettext_with_bi_tags(el)
            if gettext_with_bi_tags(el).strip() == "<b>Charter</b>":
                travelExpPg.append(pageno)
                startHeight = int(el.attrib['top'])

              
    endHeight = 1223

    print travelExpPg
    
    if not travelExpPg:
        print "No expenses available"
    else: 
        print "Found pages: " + str(travelExpPg)
    

    #Get the rows on each travel expense page
   
        for i, pageno in enumerate(travelExpPg):
            rows = []

            for val, el in enumerate(list(pages[pageno])):
            	#print el.attrib, gettext_with_bi_tags(el)
            	if gettext_with_bi_tags(el).strip() == "<b>Details</b>":
	                startHeight = int(el.attrib['top'])
            	if gettext_with_bi_tags(el).strip() == "<b>Car Costs</b>":
            		endHeight = int(el.attrib['top'])

            for val, el in enumerate(list(pages[pageno])):		
            	#print "startHeight", startHeight
                if el.tag == "text" and int(el.attrib['left']) > 45 and int(el.attrib['left']) < 48 and int(el.attrib['top']) > startHeight and int(el.attrib['top']) < endHeight:
                    rows.append(val)

            print "rows",rows
             
            for i in xrange(0, len(rows)):
                rangerows = []
                if not rows:
                    print "rows empty"
                else: 
                    for x in xrange(rows[i-1], rows[i]):
                       	rangerows.append(gettext_with_bi_tags(list(pages[pageno])[x]))
                    print rangerows
                    rowlen = len(rangerows)
                    data = {}
                    for z in xrange(0, len(rangerows)):
                        data['politician'] = politician
                        data[str(z)] = rangerows[z]
                        data['key'] = str(rows[i]) + url + str(pageno) + politician
                        data['url'] = url
                    print data
                    
                    if not data:
                       print "it's empty"
                    else: 
                       scraperwiki.sqlite.save(unique_keys=["key"], data=data)
           
            #Get the last row on each page
        
            rangerows = []
            if not rows:
                print "rows empty"
            else: 
                lastrowheight = int(list(pages[pageno])[rows[len(rows)-1]].attrib['top'])
                #236
                print "lastrowheight", lastrowheight
                for el in list(pages[pageno]):
                    if el.tag == "text" and int(el.attrib['top']) == lastrowheight:
                    	if gettext_with_bi_tags(el)[0].isdigit():
	                    	rangerows.append(gettext_with_bi_tags(el))
                    	else:	
                        	rangerows.append(gettext_with_bi_tags(el))
                #print rangerows
                data = {}
                for z in xrange(0, len(rangerows)):
                    data['politician'] = politician
                    data[str(z)] = rangerows[z]
                    data['key'] = str(rows[i]) + url + str(pageno) + politician + "Lastrow" 
                    data['url'] = url
                print data
                if not data:
                    print "it's empty"
                else: 
                    scraperwiki.sqlite.save(unique_keys=["key"], data=data)