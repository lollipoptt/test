import requests

# class TestHttp:
#     def test_get(self):
#         r=requests.get("http://httpbin.testing-studio.com/get")
#         print(r.status_code)
#         print(r.encoding)
#         print(r.content)
#         print(r.text)
#         assert r.status_code==200
#     def test_post(self):
#         r=requests.post("http://httpbin.testing-studio.com/post",data={"custtel":"15600534760"})
#         print(r.text)
#         assert r.status_code == 200

class Wework:
    def get_token(self):
        r = requests.get('https://pep-service-internal.latest.shdrapps.disney.com/profile-service/v4/clients/DPRD-SHDR.MOBILE.IOS-LATEST/guests/login',
            params = {'loginValue': '17011112222','password': 'test1234'})
        print(r.json())
        return r

    def search_inventory(self):
        r = requests.post('https://pep-service-internal.latest.shdrapps.disney.com/lexicon-view-assembler-service/product-types/shdr-theme-park/price-calendar?storeId=shdr_mobile&destinationId=shdr&affiliations=STD_GST&availStartDate=${startDateTime}&availRange=90&view=mobile',
                          params = {'authtoken':self.token})
        return r

class TestExecution:
    def test_search_inventory(self):
        r = self.Wework.search_inventory()
        self.format(r.json())
        assert r.json(['errcode'])==0