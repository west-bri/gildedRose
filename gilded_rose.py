class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

MINIMUM_QUALITY_VALUE = 0
MAXIMUM_QUALITY_VALUE = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @staticmethod
    def update_aged_brie(item: Item):
        if(item.name == 'Aged Brie' and item.quality < MAXIMUM_QUALITY_VALUE):
            item.quality = item.quality + 1
    
    @staticmethod
    def update_backstage_tickets(item:Item):
        if(item.name == 'Backstage passes to a TAFKAL80ETC concert'):
            if item.sell_in <= 0:
                item.quality = MINIMUM_QUALITY_VALUE
            elif item.sell_in <= 5: # increase quality by 3 if sellin 5 or less
                item.quality = item.quality + 3
            elif item.sell_in <= 10: # increase quality by 2 if sellin 10 or less
                item.quality = item.quality + 2
            else:
                item.quality = item.quality + 1
            
            #catch in case quality goes over 50 from addition above
            if item.quality > MAXIMUM_QUALITY_VALUE:
                item.quality = MAXIMUM_QUALITY_VALUE

    @staticmethod
    def update_item_sellin(item:Item):
        if item.name != 'Sulfuras, Hand of Ragnaros':
            item.sell_in = item.sell_in - 1
    
    @staticmethod
    def update_item_quality(item:Item):
        if item.quality > 0:
                    conjuredMultiplier = 1
                    if 'Conjured' in item.name:
                        conjuredMultiplier = 2
                    if item.sell_in < 0:
                        item.quality = item.quality - (conjuredMultiplier * 2)
                    else:
                        item.quality = item.quality - (conjuredMultiplier * 1)
                    if item.quality < MINIMUM_QUALITY_VALUE:
                        item.quality = MINIMUM_QUALITY_VALUE

    def update_quality(self):
        special_items = ['Aged Brie', 'Backstage passes to a TAFKAL80ETC concert', 'Sulfuras, Hand of Ragnaros']
        for item in self.items:
            self.update_item_sellin(item)
            if item.name in special_items:
                self.update_aged_brie(item)
                self.update_backstage_tickets(item)
            else:
                self.update_item_quality(item)
                


