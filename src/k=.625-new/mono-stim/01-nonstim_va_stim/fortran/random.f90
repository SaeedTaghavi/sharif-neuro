subroutine random_uniform(my_array,size_array,start_val,stop_val,seed)
    implicit none
    integer :: size_array
    integer :: seed
    integer :: i
    real (8) :: start_val, stop_val
    real (8) :: my_array(size_array)
    call srand(seed)
    print*,(stop_val-start_val)
    do i=1,size_array
        my_array(i) = rand()
        my_array(i) = my_array(i)*(stop_val-start_val) + start_val
    end do
end subroutine random_uniform


subroutine random_normal(my_array, size_array, mean, var, seed)
    implicit none
    integer :: size_array
    integer :: seed
    integer :: i
    real (8) :: mean, var
    real (8) :: my_array(size_array)
    call srand(seed)
end subroutine random_normal