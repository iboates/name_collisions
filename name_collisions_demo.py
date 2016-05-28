from name_collisions import find_collisions, remove_collisions

demo_list = []
demo_list.append('cherry_pie')
for i in range(1,1005):
    demo_list.append('apple_pie')
    demo_list.append('blueberry_pie')
    demo_list.append('banana_cream_pie')
    demo_list.append('some_kind_of_pie_with_a_name_so_long_that_it_is_absolutely_absurd')

for name in remove_collisions(demo_list, max_length=15, base=16):
    print(name)

collisions = find_collisions(demo_list, 10)
print(collisions)