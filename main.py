import firebase_admin
from firebase_admin import credentials, firestore
import datetime
root_collection = 'active-hosts'
##### IMPORTANT WRITE ALL OF THIS INTO A CLASS!!!!

class firebase_dns:
    def __init__(self):
        cred = credentials.Certificate('./serviceAccountKey.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def write_data_db(self,host_ip , queried_domain  , data : dict):
        self.db.collection(root_collection).document(host_ip).collection(queried_domain).add(data)

    def get_all_dns_by_host_ip(self,host_ip):
        doc_ref = self.db.collection(root_collection).document(host_ip)
        dns_data_snapshot = doc_ref.get()
        if dns_data_snapshot.exists:
            dns_data = dns_data_snapshot.to_dict()
            print(dns_data)

        for key in dns_data:
            for queried_domain in dns_data[key]:
               self.get_queried_domain_by_host( host_ip , queried_domain)
    def get_queried_domain_by_host(self,host_ip,queried_domain):
        doc_ref = self.db.collection(root_collection).document(host_ip).collection(queried_domain)
        dns_data_snapshot = doc_ref.get()  # this is duplicate code , refactor
        # returns documents , and we print them
        for snapshot in dns_data_snapshot:
            dns_data = snapshot.to_dict()
            print(dns_data)

    def get_all_dns(self):
        pass

#get_queried_domain_by_host('127.0.0.1','google.com')
#get_all_dns_by_host_ip('127.0.0.1')