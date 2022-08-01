def get_sum(a,b):
    a_plus_b = a + b
    b_to_a = b
    a_to_b = a
    if a == b:
        print(str(a) + ' (' + str(a) + ' since both are same)')
    elif a < b:
        bucket = [str(a)]
        while a != b:
            a += 1
            bucket.append(str(a))
            a_to_b += a
        bucket_string = " + ".join(bucket)
        print(str(a_to_b) + " (" + bucket_string + str(a_to_b) + ")")

    else:
        bucket = [str(b)]
        while a != b:
            b += 1
            bucket.append(str(b))
            b_to_a += b
        bucket_string = " + ".join(bucket)
        print(str(a_to_b) + " (" + bucket_string + " = " + str(b_to_a) + ")")

get_sum(3023, 30000)
