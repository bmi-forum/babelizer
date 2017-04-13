! 
! File:          f90_Component_Impl.F90
! Symbol:        f90.Component-v0.0
! Symbol Type:   class
! Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
! Description:   Server-side implementation for f90.Component
! 
! WARNING: Automatically generated; only changes within splicers preserved
! 
! 


! 
! Symbol "f90.Component" (version 0.0)
! 


#include "sidl_NotImplementedException_fAbbrev.h"
#include "f90_Component_fAbbrev.h"
#include "sidl_RuntimeException_fAbbrev.h"
#include "sidl_ClassInfo_fAbbrev.h"
#include "sidl_BaseClass_fAbbrev.h"
#include "sidl_BaseInterface_fAbbrev.h"
#include "sidl_BaseException_fAbbrev.h"
#include "csdms_core_Bmi_fAbbrev.h"
#include "sidl_int_fAbbrev.h"
#include "sidl_double_fAbbrev.h"
#include "sidl_string_fAbbrev.h"
! DO-NOT-DELETE splicer.begin(_miscellaneous_code_start)

! Insert-UserDecl-Here 

#include "gov_cca_TypeMap_fAbbrev.h"
#include "sidl_SIDLException_fAbbrev.h"

! Bocca generated code. bocca.protected.begin(_miscellaneous_code_start)


! bocca_update_exception. Used only in implementing BOCCA_SIDL_CHECK_F90
        logical function bue_f90_Component(except, meth, lin) RESULT(bue)
        use sidl
        use sidl_BaseInterface
        use sidl_RuntimeException
        implicit none
        type(sidl_BaseInterface_t) :: except, etmp
        type(sidl_RuntimeException_t) :: rex
!       logical bue
        integer lin
        character (LEN=*) meth, myfilename
        parameter(myfilename='f90_Component_Impl.F90')

        bue = .false.
        if ( not_null(except) ) then
          bue = .true.
          call cast(except, rex, etmp)
          if (not_null(rex)) then
             call add(rex, myfilename, 0_sidl_int, meth, etmp)
             call deleteRef(rex, etmp)
          endif
        endif
        return
        end

! Exit statement not normally reached (or needed) unless BOCCA_SIDL_CHECK_F90
! is used and finds an exception. 
#define BOCCAEXIT 20331

! Any method using BOCCA_SIDL_CHECK_F90 must start user code with BOCCA_EXTERNAL
! or equivalent. If the result of this macro is a line too long, the
! f90 user will have to put the equivalent in manually unless their freeform f90
! compiler supports unlimited length lines (e.g. -ffree-line-length-none).
#define BOCCA_EXTERNAL \
   external bue_f90_Component ; \
   logical bue_f90_Component

! call BOCCA_SIDL_CLEAR_F90(except)
#define BOCCA_SIDL_CLEAR_F90(except) \
  boccaClearException(self,except)

! BOCCA_SIDL_CHECK_F90(ex,methodandmessagestring) to jump to exit if
! exception ex was thrown. See SIDL_CHECK documentation for C in babel.
#define BOCCA_SIDL_CHECK_F90(except,method) \
  if ( bue_f90_Component(except, method) ) goto BOCCAEXIT

! call BOCCA_SIDL_THROW_F90(except, messagestring) 
! generate new exception and jump to exit. See SIDL_THROW doc for C in babel.
#define BOCCA_SIDL_THROW_F90(except, messagestring) \
  boccaThrowException(self, messagestring, except); \
  goto BOCCAEXIT

        
! Bocca generated code. bocca.protected.end(_miscellaneous_code_start)

! or  Insert-UserDecl-Here 

! DO-NOT-DELETE splicer.end(_miscellaneous_code_start)




! 
! Method:  _ctor[]
! Class constructor called when the class is created.
! 

recursive subroutine f90_Component__ctor_mi(self, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component._ctor.use)
  ! Insert-Code-Here {f90.Component._ctor.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component._ctor.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component._ctor)

! Insert-UserDecl-Here

! bocca-default-code. User may edit or delete.begin(f90.Component._ctor)
  ! Access private data
  type(f90_Component_wrap) :: dp
  ! Allocate memory and initialize
  allocate(dp%d_private_data) ! crash if out of memory
  
! Insert-UserCode-Here

  call f90_Component__set_data_m(self, dp)
#ifdef _BOCCA_STDERR
    write(*, *) 'CTOR f90.Component: F90 allocated'
#endif
! bocca-default-code. User may edit or delete.end(f90.Component._ctor)


! DO-NOT-DELETE splicer.end(f90.Component._ctor)
end subroutine f90_Component__ctor_mi


! 
! Method:  _ctor2[]
! Special Class constructor called when the user wants to wrap his own private data.
! 

recursive subroutine f90_Component__ctor2_mi(self, private_data, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component._ctor2.use)
  ! Insert-Code-Here {f90.Component._ctor2.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component._ctor2.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  type(f90_Component_wrap) :: private_data
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component._ctor2)
! Insert-Code-Here {f90.Component._ctor2} (_ctor2 method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component._ctor2)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component._ctor2)
! DO-NOT-DELETE splicer.end(f90.Component._ctor2)
end subroutine f90_Component__ctor2_mi


! 
! Method:  _dtor[]
! Class destructor called when the class is deleted.
! 

recursive subroutine f90_Component__dtor_mi(self, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component._dtor.use)
  ! Insert-Code-Here {f90.Component._dtor.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component._dtor.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component._dtor)

! bocca-default-code. User may edit or delete.begin(f90.Component._dtor)
  ! Access private data
  type(f90_Component_wrap) :: dp
  ! Insert-UserDecl-Here 

  call f90_Component__get_data_m(self,dp)

  ! Insert-UserCode-Here 

#ifdef _BOCCA_STDERR
    write(*, *) 'DTOR f90.Component: F90 deallocating'
#endif
  deallocate(dp%d_private_data)
! bocca-default-code. User may edit or delete.end(f90.Component._dtor)

  ! Insert-UserCode-Here , alternatively

! DO-NOT-DELETE splicer.end(f90.Component._dtor)
end subroutine f90_Component__dtor_mi


! 
! Method:  _load[]
! Static class initializer called exactly once before any user-defined method is dispatched
! 

recursive subroutine f90_Component__load_mi(exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component._load.use)
  ! Insert-Code-Here {f90.Component._load.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component._load.use)
  implicit none
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component._load)
! Insert-Code-Here {f90.Component._load} (_load method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component._load)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component._load)
! DO-NOT-DELETE splicer.end(f90.Component._load)
end subroutine f90_Component__load_mi


! 
! Method:  boccaForceUsePortInclude[]
!  This function should never be called, but helps babel generate better code. 
! 

recursive subroutine boccaForceUsePortI73_p7n3at9_mi(self, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.boccaForceUsePortInclude.use)
  ! Insert-Code-Here {f90.Component.boccaForceUsePortInclude.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.boccaForceUsePortInclude.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.boccaForceUsePortInclude)
! DO-NOT-EDIT-BOCCA
! Bocca generated code. bocca.protected.begin(f90.Component.boccaForceUsePortInclude)
  return
! Bocca generated code. bocca.protected.end(f90.Component.boccaForceUsePortInclude)
! DO-NOT-DELETE splicer.end(f90.Component.boccaForceUsePortInclude)
end subroutine boccaForceUsePortI73_p7n3at9_mi


! 
! Method:  initialize[]
! 

recursive subroutine f90_Component_initialize_mi(self, config_file, retval,    &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.initialize.use)
  ! Insert-Code-Here {f90.Component.initialize.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.initialize.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: config_file
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.initialize)
! Insert-Code-Here {f90.Component.initialize} (initialize method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.initialize)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.initialize)
! DO-NOT-DELETE splicer.end(f90.Component.initialize)
end subroutine f90_Component_initialize_mi


! 
! Method:  update[]
! 

recursive subroutine f90_Component_update_mi(self, retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.update.use)
  ! Insert-Code-Here {f90.Component.update.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.update.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.update)
! Insert-Code-Here {f90.Component.update} (update method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.update)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.update)
! DO-NOT-DELETE splicer.end(f90.Component.update)
end subroutine f90_Component_update_mi


! 
! Method:  update_until[]
! 

recursive subroutine f90_Component_update_until_mi(self, time_interval,        &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.update_until.use)
  ! Insert-Code-Here {f90.Component.update_until.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.update_until.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  real (kind=sidl_double) :: time_interval
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.update_until)
! Insert-Code-Here {f90.Component.update_until} (update_until method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.update_until)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.update_until)
! DO-NOT-DELETE splicer.end(f90.Component.update_until)
end subroutine f90_Component_update_until_mi


! 
! Method:  finalize[]
! 

recursive subroutine f90_Component_finalize_mi(self, retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.finalize.use)
  ! Insert-Code-Here {f90.Component.finalize.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.finalize.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  logical :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.finalize)
! Insert-Code-Here {f90.Component.finalize} (finalize method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.finalize)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.finalize)
! DO-NOT-DELETE splicer.end(f90.Component.finalize)
end subroutine f90_Component_finalize_mi


! 
! Method:  get_start_time[]
! 

recursive subroutine f90_Component_get_start_time_mi(self, time, retval,       &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_start_time.use)
  ! Insert-Code-Here {f90.Component.get_start_time.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_start_time.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  real (kind=sidl_double) :: time
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_start_time)
! Insert-Code-Here {f90.Component.get_start_time} (get_start_time method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_start_time)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_start_time)
! DO-NOT-DELETE splicer.end(f90.Component.get_start_time)
end subroutine f90_Component_get_start_time_mi


! 
! Method:  get_current_time[]
! 

recursive subroutine C_get_current_time78xuonyhf2_mi(self, time, retval,       &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_current_time.use)
  ! Insert-Code-Here {f90.Component.get_current_time.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_current_time.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  real (kind=sidl_double) :: time
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_current_time)
! Insert-Code-Here {f90.Component.get_current_time} (get_current_time method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_current_time)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_current_time)
! DO-NOT-DELETE splicer.end(f90.Component.get_current_time)
end subroutine C_get_current_time78xuonyhf2_mi


! 
! Method:  get_end_time[]
! 

recursive subroutine f90_Component_get_end_time_mi(self, time, retval,         &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_end_time.use)
  ! Insert-Code-Here {f90.Component.get_end_time.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_end_time.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  real (kind=sidl_double) :: time
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_end_time)
! Insert-Code-Here {f90.Component.get_end_time} (get_end_time method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_end_time)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_end_time)
! DO-NOT-DELETE splicer.end(f90.Component.get_end_time)
end subroutine f90_Component_get_end_time_mi


! 
! Method:  get_time_step[]
! 

recursive subroutine f90_Component_get_time_step_mi(self, time, retval,        &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_time_step.use)
  ! Insert-Code-Here {f90.Component.get_time_step.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_time_step.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  real (kind=sidl_double) :: time
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_time_step)
! Insert-Code-Here {f90.Component.get_time_step} (get_time_step method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_time_step)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_time_step)
! DO-NOT-DELETE splicer.end(f90.Component.get_time_step)
end subroutine f90_Component_get_time_step_mi


! 
! Method:  get_time_units[]
! 

recursive subroutine f90_Component_get_time_units_mi(self, units, retval,      &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_time_units.use)
  ! Insert-Code-Here {f90.Component.get_time_units.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_time_units.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: units
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_time_units)
! Insert-Code-Here {f90.Component.get_time_units} (get_time_units method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_time_units)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_time_units)
! DO-NOT-DELETE splicer.end(f90.Component.get_time_units)
end subroutine f90_Component_get_time_units_mi


! 
! Method:  get_component_name[]
! 

recursive subroutine get_component_name9_1i6k2f2d_mi(self, name, retval,       &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_component_name.use)
  ! Insert-Code-Here {f90.Component.get_component_name.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_component_name.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_component_name)
! Insert-Code-Here {f90.Component.get_component_name} (get_component_name method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_component_name)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_component_name)
! DO-NOT-DELETE splicer.end(f90.Component.get_component_name)
end subroutine get_component_name9_1i6k2f2d_mi


! 
! Method:  get_input_item_count[]
! 

recursive subroutine get_input_item_coubhgjirgdgy_mi(self, count, retval,      &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_input_item_count.use)
  ! Insert-Code-Here {f90.Component.get_input_item_count.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_input_item_count.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: count
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_input_item_count)
! Insert-Code-Here {f90.Component.get_input_item_count} (get_input_item_count method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_input_item_count)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_input_item_count)
! DO-NOT-DELETE splicer.end(f90.Component.get_input_item_count)
end subroutine get_input_item_coubhgjirgdgy_mi


! 
! Method:  get_output_item_count[]
! 

recursive subroutine get_output_item_cob7buunp918_mi(self, count, retval,      &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_output_item_count.use)
  ! Insert-Code-Here {f90.Component.get_output_item_count.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_output_item_count.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: count
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_output_item_count)
! Insert-Code-Here {f90.Component.get_output_item_count} (get_output_item_count method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_output_item_count)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_output_item_count)
! DO-NOT-DELETE splicer.end(f90.Component.get_output_item_count)
end subroutine get_output_item_cob7buunp918_mi


! 
! Method:  get_input_var_names[]
! 

recursive subroutine get_input_var_namejp20tibipf_mi(self, names, retval,      &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_string_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_input_var_names.use)
  ! Insert-Code-Here {f90.Component.get_input_var_names.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_input_var_names.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  type(sidl_string_1d) :: names
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_input_var_names)
! Insert-Code-Here {f90.Component.get_input_var_names} (get_input_var_names method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_input_var_names)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_input_var_names)
! DO-NOT-DELETE splicer.end(f90.Component.get_input_var_names)
end subroutine get_input_var_namejp20tibipf_mi


! 
! Method:  get_output_var_names[]
! 

recursive subroutine get_output_var_nam30phjar9y7_mi(self, names, retval,      &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_string_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_output_var_names.use)
  ! Insert-Code-Here {f90.Component.get_output_var_names.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_output_var_names.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  type(sidl_string_1d) :: names
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_output_var_names)
! Insert-Code-Here {f90.Component.get_output_var_names} (get_output_var_names method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_output_var_names)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_output_var_names)
! DO-NOT-DELETE splicer.end(f90.Component.get_output_var_names)
end subroutine get_output_var_nam30phjar9y7_mi


! 
! Method:  get_var_type[]
! 

recursive subroutine f90_Component_get_var_type_mi(self, name, type, retval,   &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_var_type.use)
  ! Insert-Code-Here {f90.Component.get_var_type.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_var_type.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  character (len=*) :: type
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_var_type)
! Insert-Code-Here {f90.Component.get_var_type} (get_var_type method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_var_type)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_var_type)
! DO-NOT-DELETE splicer.end(f90.Component.get_var_type)
end subroutine f90_Component_get_var_type_mi


! 
! Method:  get_var_units[]
! 

recursive subroutine f90_Component_get_var_units_mi(self, name, units, retval, &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_var_units.use)
  ! Insert-Code-Here {f90.Component.get_var_units.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_var_units.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  character (len=*) :: units
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_var_units)
! Insert-Code-Here {f90.Component.get_var_units} (get_var_units method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_var_units)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_var_units)
! DO-NOT-DELETE splicer.end(f90.Component.get_var_units)
end subroutine f90_Component_get_var_units_mi


! 
! Method:  get_var_nbytes[]
! 

recursive subroutine f90_Component_get_var_nbytes_mi(self, name, nbytes,       &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_var_nbytes.use)
  ! Insert-Code-Here {f90.Component.get_var_nbytes.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_var_nbytes.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  integer (kind=sidl_int) :: nbytes
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_var_nbytes)
! Insert-Code-Here {f90.Component.get_var_nbytes} (get_var_nbytes method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_var_nbytes)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_var_nbytes)
! DO-NOT-DELETE splicer.end(f90.Component.get_var_nbytes)
end subroutine f90_Component_get_var_nbytes_mi


! 
! Method:  get_var_itemsize[]
! 

recursive subroutine C_get_var_itemsize1b5ktirsq7_mi(self, name, size, retval, &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_var_itemsize.use)
  ! Insert-Code-Here {f90.Component.get_var_itemsize.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_var_itemsize.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  integer (kind=sidl_int) :: size
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_var_itemsize)
! Insert-Code-Here {f90.Component.get_var_itemsize} (get_var_itemsize method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_var_itemsize)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_var_itemsize)
! DO-NOT-DELETE splicer.end(f90.Component.get_var_itemsize)
end subroutine C_get_var_itemsize1b5ktirsq7_mi


! 
! Method:  get_var_grid[]
! 

recursive subroutine f90_Component_get_var_grid_mi(self, name, grid, retval,   &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_var_grid.use)
  ! Insert-Code-Here {f90.Component.get_var_grid.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_var_grid.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  integer (kind=sidl_int) :: grid
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_var_grid)
! Insert-Code-Here {f90.Component.get_var_grid} (get_var_grid method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_var_grid)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_var_grid)
! DO-NOT-DELETE splicer.end(f90.Component.get_var_grid)
end subroutine f90_Component_get_var_grid_mi


! 
! Method:  get_grid_type[]
! 

recursive subroutine f90_Component_get_grid_type_mi(self, grid, type, retval,  &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_type.use)
  ! Insert-Code-Here {f90.Component.get_grid_type.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_type.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  character (len=*) :: type
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_type)
! Insert-Code-Here {f90.Component.get_grid_type} (get_grid_type method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_type)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_type)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_type)
end subroutine f90_Component_get_grid_type_mi


! 
! Method:  get_grid_rank[]
! 

recursive subroutine f90_Component_get_grid_rank_mi(self, grid, rank, retval,  &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_rank.use)
  ! Insert-Code-Here {f90.Component.get_grid_rank.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_rank.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  integer (kind=sidl_int) :: rank
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_rank)
! Insert-Code-Here {f90.Component.get_grid_rank} (get_grid_rank method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_rank)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_rank)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_rank)
end subroutine f90_Component_get_grid_rank_mi


! 
! Method:  get_grid_size[]
! 

recursive subroutine f90_Component_get_grid_size_mi(self, grid, size, retval,  &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_size.use)
  ! Insert-Code-Here {f90.Component.get_grid_size.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_size.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  integer (kind=sidl_int) :: size
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_size)
! Insert-Code-Here {f90.Component.get_grid_size} (get_grid_size method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_size)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_size)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_size)
end subroutine f90_Component_get_grid_size_mi


! 
! Method:  get_grid_shape[]
! 

recursive subroutine f90_Component_get_grid_shape_mi(self, grid, shape,        &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_int_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_shape.use)
  ! Insert-Code-Here {f90.Component.get_grid_shape.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_shape.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  type(sidl_int_1d) :: shape
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_shape)
! Insert-Code-Here {f90.Component.get_grid_shape} (get_grid_shape method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_shape)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_shape)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_shape)
end subroutine f90_Component_get_grid_shape_mi


! 
! Method:  get_grid_spacing[]
! 

recursive subroutine C_get_grid_spacingnnu8or3mru_mi(self, grid, spacing,      &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_double_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_spacing.use)
  ! Insert-Code-Here {f90.Component.get_grid_spacing.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_spacing.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  type(sidl_double_1d) :: spacing
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_spacing)
! Insert-Code-Here {f90.Component.get_grid_spacing} (get_grid_spacing method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_spacing)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_spacing)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_spacing)
end subroutine C_get_grid_spacingnnu8or3mru_mi


! 
! Method:  get_grid_origin[]
! 

recursive subroutine Co_get_grid_originaoggf_a1w7_mi(self, grid, origin,       &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_double_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_origin.use)
  ! Insert-Code-Here {f90.Component.get_grid_origin.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_origin.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  type(sidl_double_1d) :: origin
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_origin)
! Insert-Code-Here {f90.Component.get_grid_origin} (get_grid_origin method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_origin)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_origin)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_origin)
end subroutine Co_get_grid_originaoggf_a1w7_mi


! 
! Method:  get_grid_x[]
! 

recursive subroutine f90_Component_get_grid_x_mi(self, grid, x, retval,        &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_double_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_x.use)
  ! Insert-Code-Here {f90.Component.get_grid_x.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_x.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  type(sidl_double_1d) :: x
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_x)
! Insert-Code-Here {f90.Component.get_grid_x} (get_grid_x method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_x)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_x)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_x)
end subroutine f90_Component_get_grid_x_mi


! 
! Method:  get_grid_y[]
! 

recursive subroutine f90_Component_get_grid_y_mi(self, grid, y, retval,        &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_double_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_y.use)
  ! Insert-Code-Here {f90.Component.get_grid_y.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_y.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  type(sidl_double_1d) :: y
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_y)
! Insert-Code-Here {f90.Component.get_grid_y} (get_grid_y method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_y)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_y)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_y)
end subroutine f90_Component_get_grid_y_mi


! 
! Method:  get_grid_z[]
! 

recursive subroutine f90_Component_get_grid_z_mi(self, grid, z, retval,        &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_double_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_z.use)
  ! Insert-Code-Here {f90.Component.get_grid_z.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_z.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  type(sidl_double_1d) :: z
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_z)
! Insert-Code-Here {f90.Component.get_grid_z} (get_grid_z method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_z)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_z)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_z)
end subroutine f90_Component_get_grid_z_mi


! 
! Method:  get_grid_vertex_count[]
! 

recursive subroutine get_grid_vertex_coqqpiwb_8g5_mi(self, grid, n_vertices,   &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_vertex_count.use)
  ! Insert-Code-Here {f90.Component.get_grid_vertex_count.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_vertex_count.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  integer (kind=sidl_int) :: n_vertices
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_vertex_count)
! Insert-Code-Here {f90.Component.get_grid_vertex_count} (get_grid_vertex_count method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_vertex_count)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_vertex_count)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_vertex_count)
end subroutine get_grid_vertex_coqqpiwb_8g5_mi


! 
! Method:  get_grid_face_count[]
! 

recursive subroutine get_grid_face_coun7bed_km_3q_mi(self, grid, n_faces,      &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_face_count.use)
  ! Insert-Code-Here {f90.Component.get_grid_face_count.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_face_count.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  integer (kind=sidl_int) :: n_faces
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_face_count)
! Insert-Code-Here {f90.Component.get_grid_face_count} (get_grid_face_count method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_face_count)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_face_count)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_face_count)
end subroutine get_grid_face_coun7bed_km_3q_mi


! 
! Method:  get_grid_connectivity[]
! 

recursive subroutine get_grid_connectivz9whr0qkch_mi(self, grid, connectivity, &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_int_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_connectivity.use)
  ! Insert-Code-Here {f90.Component.get_grid_connectivity.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_connectivity.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  type(sidl_int_1d) :: connectivity
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_connectivity)
! Insert-Code-Here {f90.Component.get_grid_connectivity} (get_grid_connectivity method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_connectivity)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_connectivity)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_connectivity)
end subroutine get_grid_connectivz9whr0qkch_mi


! 
! Method:  get_grid_offset[]
! 

recursive subroutine Co_get_grid_offset9rjb2oub9b_mi(self, grid, offset,       &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_int_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_offset.use)
  ! Insert-Code-Here {f90.Component.get_grid_offset.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_grid_offset.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  integer (kind=sidl_int) :: grid
  ! in
  type(sidl_int_1d) :: offset
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_grid_offset)
! Insert-Code-Here {f90.Component.get_grid_offset} (get_grid_offset method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_grid_offset)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_grid_offset)
! DO-NOT-DELETE splicer.end(f90.Component.get_grid_offset)
end subroutine Co_get_grid_offset9rjb2oub9b_mi


! 
! Method:  get_value[]
! 

recursive subroutine f90_Component_get_value_mi(self, name, dest, retval,      &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_array_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_value.use)
  ! Insert-Code-Here {f90.Component.get_value.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_value.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  type(sidl__array) :: dest
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_value)
! Insert-Code-Here {f90.Component.get_value} (get_value method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_value)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_value)
! DO-NOT-DELETE splicer.end(f90.Component.get_value)
end subroutine f90_Component_get_value_mi


! 
! Method:  get_value_ptr[]
! 

recursive subroutine f90_Component_get_value_ptr_mi(self, name, values,        &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_array_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_value_ptr.use)
  ! Insert-Code-Here {f90.Component.get_value_ptr.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_value_ptr.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  type(sidl__array) :: values
  ! out
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_value_ptr)
! Insert-Code-Here {f90.Component.get_value_ptr} (get_value_ptr method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_value_ptr)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_value_ptr)
! DO-NOT-DELETE splicer.end(f90.Component.get_value_ptr)
end subroutine f90_Component_get_value_ptr_mi


! 
! Method:  get_value_at_indices[]
! 

recursive subroutine get_value_at_indicy8xiwqd2vr_mi(self, name, dest, inds,   &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_array_array
  use sidl_int_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.get_value_at_indices.use)
  ! Insert-Code-Here {f90.Component.get_value_at_indices.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.get_value_at_indices.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  type(sidl__array) :: dest
  ! in
  type(sidl_int_1d) :: inds
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.get_value_at_indices)
! Insert-Code-Here {f90.Component.get_value_at_indices} (get_value_at_indices method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.get_value_at_indices)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.get_value_at_indices)
! DO-NOT-DELETE splicer.end(f90.Component.get_value_at_indices)
end subroutine get_value_at_indicy8xiwqd2vr_mi


! 
! Method:  set_value[]
! 

recursive subroutine f90_Component_set_value_mi(self, name, values, retval,    &
  exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_array_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.set_value.use)
  ! Insert-Code-Here {f90.Component.set_value.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.set_value.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  type(sidl__array) :: values
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.set_value)
! Insert-Code-Here {f90.Component.set_value} (set_value method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.set_value)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.set_value)
! DO-NOT-DELETE splicer.end(f90.Component.set_value)
end subroutine f90_Component_set_value_mi


! 
! Method:  set_value_at_indices[]
! 

recursive subroutine set_value_at_indicm006_f_b3q_mi(self, name, inds, src,    &
  retval, exception)
  use sidl
  use sidl_NotImplementedException
  use sidl_BaseInterface
  use sidl_RuntimeException
  use f90_Component
  use sidl_array_array
  use sidl_int_array
  use f90_Component_impl
  ! DO-NOT-DELETE splicer.begin(f90.Component.set_value_at_indices.use)
  ! Insert-Code-Here {f90.Component.set_value_at_indices.use} (use statements)
  ! DO-NOT-DELETE splicer.end(f90.Component.set_value_at_indices.use)
  implicit none
  type(f90_Component_t) :: self
  ! in
  character (len=*) :: name
  ! in
  type(sidl_int_1d) :: inds
  ! in
  type(sidl__array) :: src
  ! in
  integer (kind=sidl_int) :: retval
  ! out
  type(sidl_BaseInterface_t) :: exception
  ! out



! DO-NOT-DELETE splicer.begin(f90.Component.set_value_at_indices)
! Insert-Code-Here {f90.Component.set_value_at_indices} (set_value_at_indices method)
! 
! This method has not been implemented
! 

  ! DO-DELETE-WHEN-IMPLEMENTING exception.begin(f90.Component.set_value_at_indices)
  type(sidl_BaseInterface_t) :: throwaway
  type(sidl_NotImplementedException_t) :: notImpl
  call new(notImpl, exception)
  call setNote(notImpl, 'Not Implemented', exception)
  call cast(notImpl, exception,throwaway)
  call deleteRef(notImpl,throwaway)
  return
  ! DO-DELETE-WHEN-IMPLEMENTING exception.end(f90.Component.set_value_at_indices)
! DO-NOT-DELETE splicer.end(f90.Component.set_value_at_indices)
end subroutine set_value_at_indicm006_f_b3q_mi


! DO-NOT-DELETE splicer.begin(_miscellaneous_code_end)
! Insert-Code-Here {_miscellaneous_code_end} (extra code)
! DO-NOT-DELETE splicer.end(_miscellaneous_code_end)
