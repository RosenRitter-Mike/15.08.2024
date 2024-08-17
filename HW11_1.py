import statistics as st

# a
a_tup: tuple[int] = (99,);

# b
b_tup: tuple[int] = (77, 88, 99);

# c
def tup_len(tup: tuple) -> int:
    return len(tup);


print(f"test ex. c: {tup_len(b_tup)}");

# d
def plus_tup(tupa: tuple, tupb: tuple) -> tuple:
    return tupa+tupb;


print(f"test ex. d: {plus_tup(a_tup, b_tup)}");

# e
def tup_share(tup_a: tuple, tup_b: tuple) -> tuple:
    t_long: tuple = tup_a if len(tup_a) > len(tup_b) else tup_b;
    a_list: list =[num for num in t_long if num in tup_a and num in tup_b];
    return tuple(a_list);

print(f"test ex. e: {tup_share(a_tup, b_tup)}");

# f
def tup_diff(tup_a: tuple, tup_b: tuple) -> tuple:
    b_list: list = [num for num in (tup_a + tup_b) if num not in tup_share(tup_a, tup_b)];
    return tuple(b_list);

print(f"test ex. f: {tup_diff(a_tup, b_tup)}");

# g
def tup_idx(tup_a: tuple, idx: int) -> tuple:
    if abs(idx) > len(tup_a)-1:
        return None;
    else:
        return tup_a[idx];

print(f"test1 ex. g: {tup_idx(b_tup, 2)}");
print(f"test2 ex. g: {tup_idx(b_tup, -4)}");

# h
def tup_rev(tup: tuple) -> tuple:
    y: list = list(tup);
    y.reverse();
    return tuple(y);

print(f"test ex. h: {tup_rev(b_tup)}");

# i
def tup_count(tup: tuple, value: int) -> int:
    cnt: int = 0;
    div: list = [num for num in range(1,value+1) if value%num == 0];
    for n in div:
        cnt += tup.count(n);

    return cnt;

n_tup: tuple[int] = (40 ,30 ,10 ,5 ,2 ,3 ,5 ,5 ,8 ,10);
print(f"test ex. i: {tup_count(n_tup, 10)}");

# j
def multi_tup(tup: tuple, val: int) -> tuple:
    return tup * val;

print(f"test ex. j: {multi_tup(a_tup, 10)}");

# k
# def tup_w_idx1(tup: tuple) -> tuple:
#     y: list = [[i, tup[i]] for i in range(len(tup))];
#     return tuple(y);

def tup_w_idx2(tup: tuple) -> tuple:
    return tuple(enumerate(tup));

# print(f"test ex. k v.1: {tup_w_idx1(b_tup)}");
print(f"test ex. k v.2: {tup_w_idx2(b_tup)}");

# l
def tuple_mem_cnt(t: tuple) -> dict:
    cnt_dict: dict = {};
    for item in t:
        if item in cnt_dict:
            cnt_dict[item] += 1;
        else:
            cnt_dict[item] = 1;

    return cnt_dict;

def tup_stats(tup: tuple) -> dict:

    stats: dict = {
        "min": min(tup),
        "median": st.median(tup),
        "max": max(tup),
        "mean": st.mean(tup),
        "count": len(tup),
        "sort": sorted(list(tup)),
        "sort_rev": sorted(list(tup),reverse=True)
                   };
    print(stats);
    cnt_t: dict = tuple_mem_cnt(tup);
    print(cnt_t);
    return stats|cnt_t;

print(f"test ex. l: {tup_stats(n_tup)}");

# m
def tup_to_str(t: tuple) -> str:
    return ''.join(list(t));

hel_t: tuple = ("H", "E", "L", "L", "O" );
print(f"test ex. m: {tup_to_str(hel_t)}");

# n
def str_to_tup(s: str) -> tuple:
    w_list: list[str] = [c for c in s];
    return tuple(w_list);

st: str = "Hello";
print(f"test ex. n: {str_to_tup(st)}");

# o
def tup_remove(t: tuple, num: int) -> tuple:
    if num not in t:
        return t;
    else:
        y: list = list(t);
        while num in y:
            y.remove(num);

        return tuple(y);

print(f"test ex. o: {tup_remove(plus_tup(a_tup, b_tup), 99)}");

# p
def tuple_distinct(t: tuple) -> tuple:
    dis_list: list = [];
    for item in t:
        if item in dis_list:
            continue;
        else:
            dis_list.append(item);

    return tuple(dis_list);

print(f"test ex. p: {tuple_distinct(n_tup)}");

# q
def tup_apper(t: tuple, num: int) -> tuple:
    if num not in t:
        return None;
    else:
        # y: list = list(t);
        ind_list: list = [i for i in range(len(t)) if t[i] == num];

        return tuple(ind_list);

print(f"test ex. q:\n\ntup_w_idx{tup_w_idx2(n_tup)}\ntup_apper{tup_apper(n_tup, 5)}\n");

# r
def grad_tup() -> tuple:
    names: list[str] = [];
    grades: list[int] = [];
    name: str = None;
    grade: int = None;
    while True:
        name = input("input name: ");
        if name != "done":
            names.append(name);
        else:
            break;
    while True:
        grade = int(input("input grade: "));
        if grade != -999:
            grades.append(grade);
        else:
            break;

    return zip(tuple(names), tuple(grades));

temp: tuple = grad_tup();
print(f"test ex. r:{list(temp)}");