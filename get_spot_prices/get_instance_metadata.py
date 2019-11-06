import boto3
import json

def iter_over(phi,indent):
    # indent.append(' ')
    if type(phi) == dict:
      for k in phi:
       indent.append("/%s"%(k))
       print ''.join(indent[:])
       iter_over(phi[k],indent)
       indent.remove("/%s"%(k))
    elif type(phi) == list:
      for k in phi:
       print ''.join(indent[:]),k
       iter_over(k,indent)
    else:
      print ''.join(indent[:]),phi
    # indent.remove(' ')

client = boto3.client('pricing')

pagi=client.get_paginator('get_products')

# /terms/Reserved/US4KNUGYQKAD8SVF.NQ3QZPMQV9/termAttributes/OfferingClass standard
# /terms/Reserved/US4KNUGYQKAD8SVF.NQ3QZPMQV9/termAttributes/LeaseContractLength
# /terms/Reserved/US4KNUGYQKAD8SVF.NQ3QZPMQV9/termAttributes/LeaseContractLength 3yr
# /terms/Reserved/US4KNUGYQKAD8SVF.NQ3QZPMQV9/termAttributes/PurchaseOption
# /terms/Reserved/US4KNUGYQKAD8SVF.NQ3QZPMQV9/termAttributes/PurchaseOption All Upfront


gpiter=pagi.paginate(
        ServiceCode='AmazonEC2',
        Filters=[
          {
           "Type": "TERM_MATCH",
           "Field": "ServiceCode",
           "Value": "AmazonEC2"
         },
         {
           "Type": "TERM_MATCH",
           "Field": "instanceType",
           "Value": "p3.16xlarge"
           # "Value": "u-12tb1.metal"
         },
#        {
#          "Type": "TERM_MATCH",
#          "Field": "location",
#          "Value": "US East (N. Virginia)"
#         },
         {
           "Type": "TERM_MATCH",
           "Field": "operatingSystem",
           "Value": "Linux"
          },
        ],
        FormatVersion='aws_v1',
        PaginationConfig={
            "MaxItems":1000000,
            "PageSize":1
        },
)

for gp in gpiter:
 if len( gp['PriceList'] ) > 0 :
  print type(gp['PriceList'] )
  v=gp['PriceList'][0]
  j=json.loads(v)
  indent=[' ']
  iter_over(j,indent)
