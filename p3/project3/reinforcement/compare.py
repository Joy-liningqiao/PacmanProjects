import sys, os
import time
import math


'''
f0 = open("reinforcement.token","r")
lines = []
for line in f0:
	l = line.split("/")
	for word in l:
		lines.append(word)
f0.close()
print(len(lines))

f1 = open("file1.txt","w")
for word in lines:
	f1.write(word+"\n")
f1.close()

f2 = open("retest.token","r")
lines1 = []
for line in f2:
	l1 = line.split("/")
	for word1 in l1:
		lines1.append(word1)
f2.close()
print(len(lines1))

f3 = open("file2.txt","w")
for word1 in lines1:
	f3.write(word1+"\n")
f3.close()'''
import bz2, base64
line2 = str(bz2.decompress(base64.b64decode('QlpoOTFBWSZTWfnAAx8AOCpfgHkQfv///3////7////7YB08Eow+4xwO5c6Aa2xaavs7mIOeICBcPcNttB9xq6x7PhHoKPAVeVAOg7bruYw+gdzQb7Dslmh01AeCU0hAQwhlMQI9Ke0FPKYmQwE0yAPUaAaYgDTQTQIIINTEJijR5Tym1PQINNDQNAAAADU9NU1T8qeUGgANAAAyZNGhoAAD1AAACTRSJTJMgRjKaTyh5RoAHqBtTQAyAA0ZGjQIpIJoTCTT0ym1PUwamyJiZNNNMmmjQA0AAaaNAkSEaAmUxMQAqbDQNI1PTKm9T0UbU9TQD1NAAGnch9mJ80nvCP4GS/zpWL99qDE/6fyaVYixiwZ1a9pRFO7YqM+w0GLIn97X0ISsn9jPT5U4lSxR8VsLrN+W8ijJmvzMKiDFgsVeh6STCsEgxZy2HGv4/yUyeEE+euYf86elPq/FfN+0hPfe/pvhM7sEy5ui3Dy+ve/Rez3XQet1grO9fr45h6v1yWZL/693ttpoh6NO8008Nlb8Ug9iJq06yTwjtd9/kZmDnZjSIYBwVjFGREWKLAUWCDBSLBJCBITIYSEhJqe5s7zd5vPVWJqtx7HHti+vDdnix36CmhrVi3YtZ+MbEN6VmQZkR8uYfNyP4E83GmxJy1rp7SD8+jNAhxYSmXZRHqDh0U22wJneky8Wx4V57ay2wP+nUMn1M3jJbGk7UQEEoSiEhWcfY2auwFU8dgK64vM0Q4OpcA32eTcZdm4U2ZcKeqfQwwUJBBByNZxy82HO66cJt3COG+moKEA4+JmQkk7UP/NwR7RxFj2a0HYNFt/dDY06+rDcA1LO/KgWX7MKJoogkjzmtvNZ037sx0hNMcDyiFElBexSc2EhSQOmZWKoHJ0nTy8pniYUVVUWdc49J1B6iWW668S8hVacptLrM6I1PHOc5ZWLdKFvcoGyqKtko7nA0lZAly0AOFrFagISiEoT8+dZwJewHCtHE0sggggAoQSgJRu0Gs4vti8eJVZS7vxhF0VaKltoXA1OKGONPxduBNTsbFpW44Jpi213matyeV1V0XadVbyotTwVPxNhl6QpL5q8nmL/UcpwTO4n6iA7Lz7zwNwjxXavg987pWdU+Nw1VOGciXn+JtC8B7aR4xg09GfF+vyZZnYzpsDPEi7M9V3JH1+rf5OXJWV1zrQ2O9PFrgrwzRKUw3Tpu02Q14b+F8vfSZV3EubuQVrkUkITIVOJzPDxYt4rcxfvr6dS3zctjJ+jBGRNg2/U00628EDZZRboOt74PJ3lKWklNwvvQBLuxPHA0mU3crl0XGFEjdIhXxDYlFITc3DaUd+OH9vl85fZ8f17Uq6xjsy0hSI+6nNZF/LUpxefABjOQ6YtGvXd4ik4j1bS7fGY7OUDuw+n5ve9RHX0M9qtG1qJxD4sFA0SYYVdHlZyvs81b7py9+5zJu4kZeSXSXkqnsPgCgqDYl6LaD60XwUvqkFCRjJZVyCtQrhyzF+7OGSpsDAqqIWQAoCHCj6Hr0xAgILMvdtlfxz2V2mWfBrAsojM+1NzRVjk4r+BfeARUDqEY1zkPwsNaytaaUFKPcQIkLkFEVLWB6Do0s+97xZwu3jt4TXNr6pIuJ2ghU20qFehkMKXWRQ0VyJhhRzyaEYKnJOzNaXaw25C3PHs9v56cxBV/Gv0crRtpW541omIifx4FE8v0ULUMLjR15hQKX7GqfuXYEhsszEgjDMlVTiy2lRjFtVlGc6UiAsQZX6S6B1ABPnbOamMTRNtYbJNQPWwCgs/tYUZywTzHcj9D9GOSx8rP4nS9C4xl23xz6qP6ejS+nsXtbPSgVdW7cmtT2jbE5zfeoxz4CgpivHfUePhAvIx1FStmxUdmJiOv7KBafntTl1va3bwkGrvyg8Ro17LbOm0d1o8nlDSPKy9NVaFAHIuOl2gbLqjLNvEb0KKXnOeGSHRvGOmaSBUbfGG2BBYJm6FzsoaCAsjvofGzvbZIaQ/L/q38N2pjXuYlowhjzIe3ZJSaycVUL3+ajingtOKqRYophvFJbRghcEFjkfTNClfBr6i2H9BWi5jkPT8KxbZN29XS87rG2rwWcKIgLZfeE0wFenIQFrFAwbaMqL1Gg3cc+GJCONrj0ZAXQbaasCwx2QtPPFpSCI1HF1rnKqtn7UevBLwPp7e1iVhn8nawc80tel+10zqW3hF3wLyWnNG5MEwUpquHYH2Nd0QEDNCxX1QYnc9W32WWmxU/dSdAKIDT53gRftduIPtd7tyQWgUnlipduVqKQbwIs9iGVyp3ziwOvmd21lDlUIQh757bVjPuVdwUcV3hQdqaay1tiikxWjm73NuwnZEOH7lVAXqeWX1j1AIDw4hX0tloZkA248+cDOhpK510FG+Dk3X8EfNsI4VLtziMoF5gCAKUING7K1DsaZyAaT3+Hszbm04A3uw886TzKEhjD4A4GTXjaIhPxuIIfyGYfOl37F9AOJfbjFmQ25Lq+JE22Nt+Q0eA7NL5ung4QJd/fYMOzJoBaBspfZ4UWFSlDNRrWNNtGqUtnXqnG3TQ3qWPWrXPPqG1hgUF2upIII4CndutjaocSJIqRrxvS5znQW2bWXlWUz2874mPSNrb4E1w9ZuztOZ3gMBzmVli0EX6j0tdbIn4ntZ9vjKUmlJ82vL3/dT01iHGsVZ5NX/KdtpFkQFmzCkkWfCEl5mgVsDXqVxl6PL+H+et96DxkIgDY1zMAzztM+z4eVfiMdMNd6FEr7Otc8TUVhrPDotZPS9eAjg5BFfhGZ3v9/Pn5b3le2gX5dedC69Ky7wjK6qciA5dV0qqXeJMiLqA9SU9vLi0QUZlQjNl4RDUxhaM8TFeKilVgGDZ+dZl9heypZUNd4dypt+y1iOtQq9+g2BEanBuGFPjjn7sUL1MFgylj5O/g8cqSe35zb4/J7vPj83eBVQ5y1iuYPBPy5cdvf3YJRduZJiI1AVUMH13ajf45VtWJEOUFVCmsCqh4qCxAWPX99MmwEgjcm/G8eF/w/D8uDgL9w++E+EQEZCFKUJEYCMBEPQcAeAYOCCMgFKUBBBiAxIQOpOLw4TkBELLCUCFhUhhCCEBzvRtmDNCkpQSCFKiRJEggBkBIkEEKz6tGmCqhkrZx1QVUKMwxbwKqEze94KqFY6Kr9JXO7gBVQ/WQFVDFTtgqoVjU3s2v9qDJV6bAKqGZjLhWt19jD0gqoWbVU96rmBVQ19e0Z4KqErdmUS4AVUJSi7Ld6hb2qecFVCi/BVPUbkhL2PkBVQ3Ka2btdIKqFexAYNu6FLtkTRLZkymnhYLOc5hwtObnOaVK7VqYHQzAVNzGHC8q4t5i87uR0OiH4bslYxYWle3DNTbCiJJQipMMEawssDFqkly9C2ttE0mosLCXRsDS8JsY1q1ldYOstpYaiwskK62sD5/VPLnjsaRpS1XtNVhTFDSJSCIgK9HQCqhuzcoKqHACqhf5AUkgxKdfnR+jbexoj8GfXwGep6Ka2V2n3OhRy9nrewiotjabSP23nHHlfBOyPyiBrUYbLoSdkolR2DxX4fUPbnuW0ttoH1Q7Fj7UfO4Pnxf0AY3ZdkT6n2/hcYEz1kFfoQXULmsRqXyuS2TRmYSlddBzbvzE7i1bjftnxIkknbZjOwcEymhudQjCNAkEnQ9UOcNzdMbRrW7NuMaDmwhRLWl9ssAqHgD5Oz5Hrq+K+SbhXmNrqbU5dioNhOJyR4Lm2WoS2hTaYSwTMbDFqwxuX+ny/F6fV34fEWKUsSsJtDUQoIRVIny2onY0DdBfeG9esP0Dskjs0UmUQFIzeE4WR0sGu6qKYJCQhnE9zWXk8/fjJ6W/FRZaNhWG0UwxtQcCLUBvF0JwpipCbLUaJ1Pyhqi7FKLkfJ2UmTtvAlmYlF5rPf9gQLyOuAzEJ6NI5AYB3HVdlHgxTNB0nNE4VkUDxRei09NcDqUd5H5Y7MPcBCvXYE5KUVWaBs/FmH2A9WHCQBcUxQMs2JjdmJWZGH0a4nPEZl156sjaGw8BdqeZDhjcQPtIJChEiQ0oBslA2OEdhoZ34v2fb/jaYoB8blcc0jbyZtoETAhXr0gkkgwWPnjrxgSmXYERsTDNCFuBLFGQGhFnXsgYC+STMWZMggUq/LqCZo15MMqIeDGUYZ5psKsc+P6oEDrrg1LaLcQZl+SBwlKG0GUB7YxA4xgCCQFO6XJRRzCRA4RO8xZccSJrGdpcx1QXnexq0FDhQ97zD2/pEp2dz3A8/WchVW0KVq1HzCUMbScBIJBCNLRa/0SsCfFAac7s9SWWSqs6Ax0mzy1LCyA9CHWywggF25A97V+2Fs6Lk29XSitULaEtqwQa/xAcbXODBl7cyIXREkX2mEvgvR8k+0UtoVCnyyBZSw9owQYpeIrYTRgxCnBYDLCYZEYD+b6IdPzvq/PiW8s95s/OOhP/ifX3A49dzSTBWDFivrgqoTVJFOtlxOi4cLe9nFqJPQYUCypjWImOPSIJiYkSzA7Dck7Eg8++yc78xhpT05YWsGwfbYhZopcbywOihsdV6LZgHez5ahkg2aSZ744jx6k82ViCM+bzgMfVVdrB/sg+S6gYx12rC0VHZbJzei2eXuujUfRWVPfyRdiFSQiEBIrJHqeBpV6RCu1ilJTuAqt3EiwdzIrFCNr+9LgQcsqVDhUQEdChQxBIe5rnKskmjK+tNLaKAiIkFhUbJFxCVFqDWcxTSkL7sp81spBtAj8SVao7NZvb5qSsdXlJQFKdWgGKDoQd/rgBoMsRJHRcjm7uJwCfKwRXoWZbf7ybYQB2Z9fb08/ILGHDdc2ENWtLOXVQgIzy1TsVm20zkaLWDD7pUacWeFkhtSTkxSiQSJkQRkjTBTC0Uc+V9Rb0DVC/c+3GBdZSSckEJwiIoS1oM3lLTNh8epBZfrdf/8SJ+AjA4t+Y1NkgppMi3XV2EmKjx3tR9DFlAr8WiqAvrdFUmSvmIvkAYFoH9NP1WgBWqgv4C2cRjKdiaB0I6V0bqyA7UhobDIQAgEMiPpk51ce1qOuDw9DzJherJt6wFJnlyLQ8RZhMJ9v6ipl1LbJeihCgxLEtZqfDYBKc/aURNP3xS+42gkkgsKetMG0MaB7A79R0QZli684JKxW7t0dk4k0GtHSQE2O6Amfrad/TptZP3AwUEWl0pwKM+O883jJ28w18czhR4u1aUNjHe6A2eZTl6ePTzprw6xbUt2zgx4bXrFHqE3OsKvUWLK7FbBmGohilhRyoW9WWcy1Sopw0y6jriGwRtUEyCJSFxahryJRg2VlmkxKkjSY0pOskiiD7ln4CPlvdk+2nqJw9Q/QLlFvOWyBStSm0cRnlvvOY1Y80m4hw4iIhazDAuo6iWgYpLJA3xQE+wWQoxkY6zCB+TEQFCII0N3V7CYWK1kXJgiCIyaFi+XlKKTnBVQzr6T6QKqEjZmc8hjmxpXmnxuEE2dftUcegpcQsRawBZv2wvd6ANYhCaG11XrSCZnd9tNqdoLBKzvTZ6Cv1a3MBsQTUIHbhaQQugFwVvg4jA1WKp4upzysprfkyhvNAfee0N+O3nG0TZwlxciJPIcWDGmSlDntv37vUBsz9N4AZFyKxsTQ2m2IGNjTQ/Ygof3wbLUZpB0vtOAb8WdjWOnofgq3GAt6PnhIkDAeUBqV2+CXKeeBdOpv0cubGtrUjsBJJB3GYLZscs/CsqUhdX8QSSQWWgzTrFIRYGBV4X88+EXrKtzkg9GAaDUNQgGnEdsEDINQSSQSm/YjC0PtxJhuLxs1YIxaRiH9XqjImrOaFNoV15lMRN8qjrmprqOm7p8crDjx2C3rYwM7jjaIPiOO15TsoTG2uzOOZczGSTw0lZMWmVGazkwPt0gDVEBvoHQW3yNlkyWxwpmyiIlPuBJJBzLzcszuZruvg93dJI30WzSM5vcEogvhQwaQMQwGQcWXRtYpMNrlPnsrwMDDfiS6V7YsDNHQBiAxXbLxHCo/hUJvEA+IyVswbNnxy3PiYLo2+y7BM4hDBvIhkDGYsglA4IvBxhFERWDJnF9Wdw5U+9ArE+KecIScC/Mh4sMakf7M5FJlSVICEBkFJXZ1Vr0yWTbJxC4G69FAG0XIvk5EDQYECJIEhkdcFVCAk3KCbIQTwilKBiqmgrZol4it4gtZ28OD5xhtGBzLw+PNdimI1chtAySMIelk4wQrL76SckY9H0z+B7fhd+9fsx+MGZmYNbNjt9JA3RB2vGkJJQ4zSasDGjsSQ1gNQcwMecGc5J6Xqnzo/6U/w2uYtg7QuVv1OzEpdBq0DYkSlDYiYcq/E6FdbarUSZsC+Pf59vDjS/yo0CguLtswsRVDrYvb6BWBsaRUEURhz5B2Z2VSOTJ+S5jXQrP8hznRpjDnXr8ffdlXEOcX1+Qz9j6D9P5ZPmQv0M3s36vL7ZivslM39mmicThsULrQxucvLqbVfqxVFh1eIJMqi8ssyFVqoqqqNGrQqq1LEEgiSqqqt+b6+dT4t3z+hqMR0SnE7YFmngyl5R8CHkhSQSVkzOmmSJeCCRx4yGFeMvaJZmmsn9bx6cwder07TxruGzjTzeM5Wyc0uRdDZ6fR1weuJ4e3oQdanb0Iodcl7odIZYjM1OWkrXj0Im5jiLvLtqta8a8WPOVt0GvdwWnU5wijmyfShzcJ52q8kePHDzxa5o4fDwH0Bjm4K9PbgfUTQkiLpDvByCIIV3Ra2zu5msWrhZpp+ATC9HKbdmUf3ZI016ijFjskJE7avjVajEJs8Gxhk6329Yi5GSCi6eGN1pmID6vdPKw8wJJIJEqCMDPueVfRJUfXG22SL60o+bQ8m+DhiWeG2oQtaxdAJJILZBRkOFYB94B+YzDFAX/YATuuV7yGSBlUuGVkqQUguiC9GPoFmKnLFfcVRM6w916zGOmUJJdDv4Z2aA1h3UlOZRMsACD3GtiKCHgmAMANaoqIu8T3KmA9Vhz1xwD5KA0CSRAVDNKGgzaaeHl99SZRpTDEzD9ut32qPmJmecK0HRTKqU0HM7tPAHORHGs3BR/fpqryYSCFX0KA3URnYb1AF1EKGui3m6eUXjKsuhQAxXIIffIzERSRSJSCx/AEkkDpjlesbQklolbr3Poc9A4ERVQMGQEKxdzPTld5h3X2X2on+4bTMsKeCAkBouAWE6H7b8PNPK9JVwhMaAbWHDTforsdxuj5jpcaittBtRCfdRUYcmgDF9Zb67fjAoGOhfgPO/e1cDiuK3GOVJ7EIeLZyVBPrK1qlVewqe9A2pTBcDXrG0bdVjwoVjwowVlrvTQqUdBZAo6jc1KXS3y2OJPP0nWinbLGEKvR1yVhxtOQVgtATd075Z0MOkZzo3UielPqMTBPE9bgCtAPumN9dHvNgVYBoZ9HJUiDTRQnksNa4I+rCHn0sH145BS7AEVSYGDGpIDi11ltmAZqJ60OXo33dRu3hvaY0FqDmma7tpxnN0NMa+u6a3l3uSdBHyTkNGHlIUe09h8/yQ4lgOqHuyMxrJiIQPbEh9CRorU5ABPEx/MEkkGK5y9XckGFA6ZgE89Vy0JQpn4iI0g/QfwB2SyXVh1Axet4O06bENfwqcu9KJylJH7wSSQXXLms7ayADtCqRTrHTvjePXz768hl9xZxRXrMr8qBJh2oKmsxot4uK4hDNXxqt+BktFG1SrJawSSQRPOmPmJyyYTXq/eCSSDOyw4FouiZW5QlMWVoS1Ok/LbwBJJBlUXk0mHV3HfG/pkpJys8dddcknhIYLOtyGgMKz2Pkmp9zrx4J12AkkgeiI3omX/CyGezia2Ck2SbO2UoJEKmdGYTa5tHalGy4xk/lPdLzrotCtV2K50garYlKkrawYfCMoWAIwFhsNkFxWSgsm5LqmO7Nzmc2ExSkoK2QxgDI1WWLWHDo64LSxqSxV4GsIDSYpYeIfEc4+CSyp1a2LXGrHXVJNloVioOGBRVk2Ww9fQD9v3z4Dx5HPuoewPB6y1Y5J7Axdx2MyMr60807p/Y9x9Lz5hBz4SBBCAVAAf4u5IpwoSHzgAY+A=')))
splitline = line2.split("\n")
splitLine = []
for line in splitline:
	s = line.split("\\n")
	for a in s:
		splitLine.append(a)

f3 = open("file3.txt","w")
for word1 in splitLine:
	f3.write(word1+"\n")
f3.close()