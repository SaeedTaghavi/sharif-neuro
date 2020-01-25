program kuramoto
implicit none
integer, parameter :: Nosc = 6
integer :: i, it
integer :: seed
real (8), parameter :: pi=4.0d0*datan(1.0d0)
real (8) :: theta0(Nosc)
real (8) :: theta(Nosc)
real (8) :: DthetaDt(Nosc)
real (8) :: k
real (8) :: omega
real (8) :: dt
real (8) :: test(Nosc)
real (8) :: start_val, stop_val
seed = 1
start_val=5.0
stop_val=10.0
call random_uniform(test,Nosc,start_val,stop_val,seed)
print*,test
call random_uniform(test,Nosc,start_val,stop_val,seed)
print*,test
end program kuramoto
