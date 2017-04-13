! 
! File:          f90_Component_Mod.F90
! Symbol:        f90.Component-v0.0
! Symbol Type:   class
! Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
! Description:   Server-side private data module for f90.Component
! 
! WARNING: Automatically generated; only changes within splicers preserved
! 
! 

#include "sidl_BaseInterface_fAbbrev.h"
#include "f90_Component_fAbbrev.h"

! DO-NOT-DELETE splicer.begin(_hincludes)
! Insert-Code-Here {_hincludes} (include files)
! DO-NOT-DELETE splicer.end(_hincludes)

module f90_Component_impl

  ! DO-NOT-DELETE splicer.begin(f90.Component.use)
  ! Insert-Code-Here {f90.Component.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.use)

  private :: wrapObj_s

  interface wrapObj
  module procedure wrapObj_s
  end interface

  type f90_Component_priv
    sequence
    ! DO-NOT-DELETE splicer.begin(f90.Component.private_data)
    ! Insert-Code-Here {f90.Component.private_data} (private data members)
    integer :: place_holder ! replace with your private data
    ! DO-NOT-DELETE splicer.end(f90.Component.private_data)
  end type f90_Component_priv

  type f90_Component_wrap
    sequence
    type(f90_Component_priv), pointer :: d_private_data
  end type f90_Component_wrap

  contains

  recursive subroutine wrapObj_s(private_data, retval, exception)
    use f90_Component
    use sidl_BaseInterface
    implicit none
    ! out f90_Component retval
    type(f90_Component_t) , intent(out) :: retval
    ! out sidl_BaseInterface exception
    type(sidl_BaseInterface_t) , intent(out) :: exception
    ! in f90_Component_wrap private_data
    type(f90_Component_wrap), intent(in) :: private_data
    external f90_Component_wrapObj_m
    call f90_Component_wrapObj_m(private_data, retval, exception)
   end subroutine wrapObj_s
end module f90_Component_impl
