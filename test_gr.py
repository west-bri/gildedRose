import gilded_rose as gr

def test_vacuous():
    assert True

# All items have a SellIn value which denotes the number of days we have to sell the items
# All items have a Quality value which denotes how valuable the item is
# At the end of each day our system lowers both values for every item
def test_update_item_sellin_and_quality():
    testItem = gr.Item('Test',10,40)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality == 39 and shop.items[0].sell_in == 9

# Once the sell by date has passed, Quality degrades twice as fast
def test_past_sell_by_quality_degrades_twice_as_fast():
    testItem = gr.Item('Test',0,40)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality == 38

# The Quality of an item is never negative
def test_quality_never_negative():
    testItem = gr.Item('Test',100,0)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality > -1

# "Aged Brie" actually increases in Quality the older it gets
def test_aged_brie_quality_increases():
    testItem = gr.Item('Aged Brie',50,10)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality ==11

# The Quality of an item is never more than 50
#BRW: I don't see anything preventing an item coming in with a value greater than 50
def test_value_cant_exceed_50():
    testItem = gr.Item('Aged Brie',50,50)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality == 50

# "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
def test_sulfuras_quality_sell_by_never_decrease():
    testItem = gr.Item('Sulfuras, Hand of Ragnaros',sell_in= 10, quality=40)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    print(shop.items[0])
    assert (shop.items[0].quality == 40) & (shop.items[0].sell_in == 10)

# "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
def test_backstage_passes_quality_increases():
    testItem = gr.Item('Backstage passes to a TAFKAL80ETC concert',50,10)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality ==11
# Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
def test_backstage_passes_quality_increases_by_two_sellin_10_or_less():
    testItem = gr.Item('Backstage passes to a TAFKAL80ETC concert',10,10)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality == 12
# Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
def test_backstage_passes_quality_increases_by_three_sellin_5_or_less():
    testItem = gr.Item('Backstage passes to a TAFKAL80ETC concert',5,10)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality == 13
# Quality drops to 0 after the concert
def test_backstage_passes_quality_goes_to_zero_after_sellin():
    testItem = gr.Item('Backstage passes to a TAFKAL80ETC concert',0,10)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality == 0

#"Conjured" items degrade in Quality twice as fast as normal items
def test_conjured_items_degrade_twice_as_fast():
    testItem = gr.Item('Conjured Test Item',10,10)
    shop = gr.GildedRose([testItem])
    shop.update_quality()
    assert shop.items[0].quality == 8