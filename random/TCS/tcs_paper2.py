def bidProperty(list_of_property, list_of_tender):
    # tenders = {k: k.property_type for k in list_of_tender}
    p_index = []
    p_obj = {}
    for k in list_of_property:
        p_index.append(k.property_type)
        p_obj[k.property_type] = k
    # todo: validate tender
    bid_tname = {k: "" for k in p_obj.keys()}
    bid_ptype = {k: v.property_value for k, v in p_obj.items()}
    for tender in list_of_tender:
        if tender.propertyType in p_obj:
            prop_obj = p_obj[tender.propertyType]
            if tender.bidPrice < prop_obj.max_bid_price and tender.bidPrice > \
                    bid_ptype[prop_obj.property_type]:
                bid_ptype[prop_obj.property_type] = tender.bidPrice
                bid_tname[prop_obj.property_type] = tender.buyerName
                #todo : replace p_index with list_of_property iteration
                if prop_obj.property_type in p_index:
                    index = p_index.index(prop_obj.property_type)
                    list_of_property.pop(index)
                    p_index.pop(index)
    if len(bid_tname) > 0:
        return [v for k, v in bid_tname.items() if v !=""]
    return None


class Property:
    def __init__(self, property_type, property_value, max_bid_price):
        self.property_type = str(property_type).lower()
        self.property_value = int(property_value)
        self.max_bid_price = int(max_bid_price)


class Tender:
    def __init__(self, buyerName, propertyType, bidPrice):
        self.buyerName = str(buyerName)
        self.propertyType = str(propertyType).lower()
        self.bidPrice = int(bidPrice)


if __name__ == '__main__':
    num_of_property_objects = int(input())
    list_of_property_objects = []
    for i in range(0, num_of_property_objects):
        p_type = str(input())
        p_val = int(input())
        max_b = int(input())
        list_of_property_objects.append(Property(p_type, p_val, max_b))
    num_of_tender_objects = int(input())
    list_of_tender_objects = []
    for i in range(0, num_of_tender_objects):
        t_name = str(input())
        p_type = str(input())
        b_price = int(input())
        list_of_tender_objects.append(Tender(t_name, p_type, b_price))
    print(bidProperty(list_of_property=list_of_property_objects,
                list_of_tender=list_of_tender_objects))
