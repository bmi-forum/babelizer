/*
 * File:          c_Component_Impl.c
 * Symbol:        c.Component-v0.0
 * Symbol Type:   class
 * Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
 * Description:   Server-side implementation for c.Component
 * 
 * WARNING: Automatically generated; only changes within splicers preserved
 * 
 */

/*
 * DEVELOPERS ARE EXPECTED TO PROVIDE IMPLEMENTATIONS
 * FOR THE FOLLOWING METHODS BETWEEN SPLICER PAIRS.
 */

/*
 * Symbol "c.Component" (version 0.0)
 */

#include "c_Component_Impl.h"
#include "sidl_NotImplementedException.h"
#include "sidl_Exception.h"
#ifndef included_sidl_MemAllocException_h
#include "sidl_MemAllocException.h"
#endif

/* DO-NOT-DELETE splicer.begin(c.Component._includes) */

/* Insert-UserCode-Here {c.Component._includes} (includes and arbitrary code) */

/* Bocca generated code. bocca.protected.begin(c.Component._includes) */
#include <stdlib.h>
#include <string.h>
#include "sidl_SIDLException.h"

#define _BOCCA_CTOR_MESSAGES 0

#ifdef _BOCCA_STDERR

#define BOCCA_FPRINTF fprintf
#include <stdio.h>
#include "sidl_String.h"
#ifdef _BOCCA_CTOR_PRINT
#undef _BOCCA_CTOR_MESSAGES
#define _BOCCA_CTOR_MESSAGES 1
#endif /* _BOCCA_CTOR_PRINT */

#else /* _BOCCA_STDERR */
#define BOCCA_FPRINTF boccaPrintNothing
#endif /* _BOCCA_STDERR */

static int
boccaPrintNothing(void *v, const char * s, ...)
{
  (void)v; (void)s;
  return 0;
}
/* Bocca generated code. bocca.protected.end(c.Component._includes) */

/* Insert-UserCode-Here {c.Component._includes} (includes and arbitrary code) */

/* DO-NOT-DELETE splicer.end(c.Component._includes) */

#define SIDL_IOR_MAJOR_VERSION 2
#define SIDL_IOR_MINOR_VERSION 0
/*
 * Static class initializer called exactly once before any user-defined method is dispatched
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component__load"

#ifdef __cplusplus
extern "C"
#endif
void
impl_c_Component__load(
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component._load) */
    /* Insert-Code-Here {c.Component._load} (static class initializer method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(c.Component._load) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(c.Component._load) */
    /* DO-NOT-DELETE splicer.end(c.Component._load) */
  }
}
/*
 * Class constructor called when the class is created.
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component__ctor"

#ifdef __cplusplus
extern "C"
#endif
void
impl_c_Component__ctor(
  /* in */ c_Component self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
  /* DO-NOT-DELETE splicer.begin(c.Component._ctor) */

  /* Insert-UserDecl-Here {c.Component._ctor} (constructor method) */
    
  /* bocca-default-code. User may edit or delete.begin(c.Component._ctor) */
   struct c_Component__data *dptr = 
       (struct c_Component__data*)malloc(sizeof(struct c_Component__data));
   if (dptr) {
      memset(dptr, 0, sizeof(struct c_Component__data));
   }
   c_Component__set_data(self, dptr);

   {
     dptr->state = (BMI_Model*) calloc(1, sizeof(BMI_Model));
     ${bmi_register} (dptr->state);
   }

   #if _BOCCA_CTOR_MESSAGES
     BOCCA_FPRINTF(stderr, 
        "CTOR c.Component: %s constructed data %p in self %p\n", 
        __FUNC__, dptr, self);
   #endif /* _BOCCA_CTOR_MESSAGES */
  /* bocca-default-code. User may edit or delete.end(c.Component._ctor) */

  /* initialize user elements of dptr here */
  /* Insert-UserCode-Here {c.Component._ctor} (constructor method) */

  /* DO-NOT-DELETE splicer.end(c.Component._ctor) */
  }
}

/*
 * Special Class constructor called when the user wants to wrap his own private data.
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component__ctor2"

#ifdef __cplusplus
extern "C"
#endif
void
impl_c_Component__ctor2(
  /* in */ c_Component self,
  /* in */ void* private_data,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component._ctor2) */
    /* Insert-Code-Here {c.Component._ctor2} (special constructor method) */
    /*
     * This method has not been implemented
     */

    /* DO-DELETE-WHEN-IMPLEMENTING exception.begin(c.Component._ctor2) */
    SIDL_THROW(*_ex, sidl_NotImplementedException,     "This method has not been implemented");
  EXIT:;
    /* DO-DELETE-WHEN-IMPLEMENTING exception.end(c.Component._ctor2) */
    /* DO-NOT-DELETE splicer.end(c.Component._ctor2) */
  }
}
/*
 * Class destructor called when the class is deleted.
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component__dtor"

#ifdef __cplusplus
extern "C"
#endif
void
impl_c_Component__dtor(
  /* in */ c_Component self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
  /* DO-NOT-DELETE splicer.begin(c.Component._dtor) */

  /* deinitialize user elements of dptr here */
  /* Insert-UserCode-Here {c.Component._dtor} (destructor method) */
    
  /* bocca-default-code. User may edit or delete.begin(c.Component._dtor) */
   struct c_Component__data *dptr = 
                c_Component__get_data(self);
   if (dptr) {
      free(dptr);
      c_Component__set_data(self, NULL);
   }
   #if _BOCCA_CTOR_MESSAGES
     BOCCA_FPRINTF(stderr, "DTOR c.Component: %s freed data %p in self %p\n", 
                   __FUNC__, dptr, self);
   #endif /* _BOCCA_CTOR_MESSAGES */
  /* bocca-default-code. User may edit or delete.end(c.Component._dtor) */

  /* DO-NOT-DELETE splicer.end(c.Component._dtor) */
  }
}

/*
 *  This function should never be called, but helps babel generate better code. 
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_boccaForceUsePortInclude"

#ifdef __cplusplus
extern "C"
#endif
void
impl_c_Component_boccaForceUsePortInclude(
  /* in */ c_Component self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
  /* DO-NOT-DELETE splicer.begin(c.Component.boccaForceUsePortInclude) */
/* DO-NOT-EDIT-BOCCA */
  /* Bocca generated code. bocca.protected.begin(c.Component.boccaForceUsePortInclude) */
    (void)self;

  /* Bocca generated code. bocca.protected.end(c.Component.boccaForceUsePortInclude) */
  /* DO-NOT-DELETE splicer.end(c.Component.boccaForceUsePortInclude) */
  }
}

/*
 * Method:  initialize[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_initialize"

#ifdef __cplusplus
extern "C"
#endif
sidl_bool
impl_c_Component_initialize(
  /* in */ c_Component self,
  /* in */ const char* config_file,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.initialize) */
    BMI_Model * model = GET_BMI_MODEL(self);
    model->initialize(config_file, &(model->self));

    return 0;

  EXIT:;
    return 1;
    /* DO-NOT-DELETE splicer.end(c.Component.initialize) */
  }
}

/*
 * Method:  update[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_update"

#ifdef __cplusplus
extern "C"
#endif
sidl_bool
impl_c_Component_update(
  /* in */ c_Component self,
  /* in */ double time_interval,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.update) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->update(model->self);
    /* DO-NOT-DELETE splicer.end(c.Component.update) */
  }
}

/*
 * Method:  update_until[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_update_until"

#ifdef __cplusplus
extern "C"
#endif
sidl_bool
impl_c_Component_update_until(
  /* in */ c_Component self,
  /* in */ double time_interval,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.update_until) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->update_until(model->self, time_interval);
    /* DO-NOT-DELETE splicer.end(c.Component.update_until) */
  }
}


/*
 * Method:  finalize[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_finalize"

#ifdef __cplusplus
extern "C"
#endif
sidl_bool
impl_c_Component_finalize(
  /* in */ c_Component self,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.finalize) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->finalize(model->self);
    /* DO-NOT-DELETE splicer.end(c.Component.finalize) */
  }
}

/*
 * Method:  get_start_time[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_start_time"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_start_time(
  /* in */ c_Component self,
  /* out */ double* time,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_start_time) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_start_time(model->self, time);
    /* DO-NOT-DELETE splicer.end(c.Component.get_start_time) */
  }
}

/*
 * Method:  get_current_time[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_current_time"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_current_time(
  /* in */ c_Component self,
  /* out */ double* time,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_current_time) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_current_time(model->self, time);
    /* DO-NOT-DELETE splicer.end(c.Component.get_current_time) */
  }
}

/*
 * Method:  get_end_time[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_end_time"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_end_time(
  /* in */ c_Component self,
  /* out */ double* time,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_end_time) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_end_time(model->self, time);
    /* DO-NOT-DELETE splicer.end(c.Component.get_end_time) */
  }
}

/*
 * Method:  get_time_step[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_time_step"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_time_step(
  /* in */ c_Component self,
  /* out */ double* time,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_time_step) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_time_step(model->self, time);
    /* DO-NOT-DELETE splicer.end(c.Component.get_time_step) */
  }
}

/*
 * Method:  get_time_units[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_time_units"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_time_units(
  /* in */ c_Component self,
  /* out */ char** units,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_time_units) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    *units = (char*) malloc(sizeof(char) * 2048);
    status = model->get_time_units(model->self, *units);
    if (status != 0)
        free(*units);
    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_time_units) */
  }
}

/*
 * Method:  get_component_name[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_component_name"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_component_name(
  /* in */ c_Component self,
  /* out */ char** name,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_component_name) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    *name = (char*)malloc(sizeof(char) * 2048);

    status = model->get_component_name(model->self, *name);
    if (status != 0)
        free(*name);
    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_component_name) */
  }
}

/*
 * Method:  get_input_item_count[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_input_item_count"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_input_item_count(
  /* in */ c_Component self,
  /* out */ int32_t* count,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_input_item_count) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_input_var_name_count(model->self, count);
    /* DO-NOT-DELETE splicer.end(c.Component.get_input_item_count) */
  }
}

/*
 * Method:  get_output_item_count[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_output_item_count"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_output_item_count(
  /* in */ c_Component self,
  /* out */ int32_t* count,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_output_item_count) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_output_var_name_count(model->self, count);
    /* DO-NOT-DELETE splicer.end(c.Component.get_output_item_count) */
  }
}

/*
 * Method:  get_input_var_names[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_input_var_names"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_input_var_names(
  /* in */ c_Component self,
  /* out array<string> */ struct sidl_string__array** names,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_input_var_names) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    int number_of_names = 0;

    status = model->get_input_var_name_count(model->self, &number_of_names);
    if (status != 0)
        return status;

    *names = sidl_string__array_create1d(number_of_names);

    {
      int i;
      char **item_names = NULL;

      item_names = (char**)malloc(sizeof(char*) * number_of_names);
      item_names[0] = (char*)calloc(number_of_names * 2048, sizeof(char));
      for (i = 1; i < number_of_names; i ++) {
        item_names[i] = item_names[i - 1] + 2048;
      }

      status = model->get_input_var_names(model->self, item_names);
      if (status != 0) {
          free(item_names);
          return status;
      }

      for (i = 0; i < number_of_names; i ++) {
        sidl_string__array_set1(*names, i, item_names[i]);
      }
      free(item_names);
    }

    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_input_var_names) */
  }
}

/*
 * Method:  get_output_var_names[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_output_var_names"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_output_var_names(
  /* in */ c_Component self,
  /* in array<string> */ struct sidl_string__array* names,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_output_var_names) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    int number_of_names = 0;

    status = model->get_output_var_name_count(model->self, &number_of_names);
    if (status != 0)
        return status;

    *names = sidl_string__array_create1d(number_of_names);

    {
      int i;
      char **item_names = NULL;

      item_names = (char**)malloc(sizeof(char*) * number_of_names);
      item_names[0] = (char*)calloc(number_of_names * 2048, sizeof(char));
      for (i = 1; i < number_of_names; i ++) {
        item_names[i] = item_names[i - 1] + 2048;
      }

      status = model->get_output_var_names(model->self, item_names);
      if (status != 0) {
        free(item_names);
        return status;
      }

      for (i = 0; i < number_of_names; i ++) {
        sidl_string__array_set1(*names, i, item_names[i]);
      }
      free(item_names);
    }

    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_output_var_names) */
  }
}

/*
 * Method:  get_var_type[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_var_type"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_var_type(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ char** type,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_var_type) */
    int status;

    BMI_Model * model = GET_BMI_MODEL(self);
    *type = (char*) malloc(sizeof(char) * 2048);
    status = model->get_var_type(model->self, name, *type);
    if (status != 0)
        free(*type);
    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_var_type) */
  }
}

/*
 * Method:  get_var_units[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_var_units"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_var_units(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ char** units,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_var_units) */
    int status;

    BMI_Model * model = GET_BMI_MODEL(self);
    *units = (char*) malloc(sizeof(char) * 2048);
    status = model->get_var_units(model->self, name, *units);
    if (status != 0)
        free(*units);
    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_var_units) */
  }
}

/*
 * Method:  get_var_nbytes[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_var_nbytes"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_var_nbytes(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ int32_t* nbytes,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_var_nbytes) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_var_nbytes(model->self, name, nbytes);
    /* DO-NOT-DELETE splicer.end(c.Component.get_var_nbytes) */
  }
}

/*
 * Method:  get_var_itemsize[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_var_itemsize"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_var_itemsize(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ int32_t* size,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_var_itemsize) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_var_itemsize(model->self, name, size);
    /* DO-NOT-DELETE splicer.end(c.Component.get_var_itemsize) */
  }
}

/*
 * Method:  get_var_grid[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_var_grid"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_var_grid(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ int32_t* grid,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_var_grid) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_var_grid(model->self, name, grid);
    /* DO-NOT-DELETE splicer.end(c.Component.get_var_grid) */
  }
}

/*
 * Method:  get_grid_type[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_type"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_type(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ char** type,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_type) */
    int status;

    BMI_Model * model = GET_BMI_MODEL(self);
    *type = (char*)malloc(sizeof(char) * 2048);
    status = model->get_grid_type(model->self, grid, *type);
    if (status != 0)
        return -1;
    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_type) */
  }
}

/*
 * Method:  get_grid_rank[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_rank"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_rank(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ int32_t* rank,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_rank) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_grid_rank(model->self, grid, rank);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_rank) */
  }
}

/*
 * Method:  get_grid_size[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_size"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_size(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ int32_t* size,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_size) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_grid_size(model->self, grid, size);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_size) */
  }
}

/*
 * Method:  get_grid_shape[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_shape"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_shape(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* shape,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_shape) */
    BMI_Model * model = GET_BMI_MODEL(self);
    int * buffer = sidl_int__array_first(shape);

    return model->get_grid_shape(model->self, grid, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_shape) */
  }
}

/*
 * Method:  get_grid_spacing[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_spacing"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_spacing(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* spacing,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_spacing) */
    BMI_Model * model = GET_BMI_MODEL(self);
    double * buffer = sidl_double__array_first(spacing);

    return model->get_grid_spacing(model->self, grid, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_spacing) */
  }
}

/*
 * Method:  get_grid_origin[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_origin"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_origin(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* origin,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_origin) */
    BMI_Model * model = GET_BMI_MODEL(self);
    double * buffer = sidl_double__array_first(origin);

    return model->get_grid_origin(model->self, grid, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_origin) */
  }
}

/*
 * Method:  get_grid_x[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_x"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_x(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<double> */ struct sidl_double__array* x,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_x) */
    BMI_Model * model = GET_BMI_MODEL(self);
    double * buffer = sidl_double__array_first(x);

    return model->get_grid_x(model->self, grid, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_x) */
  }
}

/*
 * Method:  get_grid_y[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_y"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_y(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<double> */ struct sidl_double__array* y,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_y) */
    BMI_Model * model = GET_BMI_MODEL(self);
    double * buffer = sidl_double__array_first(y);

    return model->get_grid_y(model->self, grid, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_y) */
  }
}

/*
 * Method:  get_grid_z[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_z"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_z(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<double> */ struct sidl_double__array* z,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_z) */
    BMI_Model * model = GET_BMI_MODEL(self);
    double * buffer = sidl_double__array_first(z);

    return model->get_grid_z(model->self, grid, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_z) */
  }
}

/*
 * Method:  get_grid_vertex_count[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_vertex_count"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_vertex_count(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ int32_t* n_vertices,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_vertex_count) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_grid_vertex_count(model->self, grid, n_vertices);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_vertex_count) */
  }
}

/*
 * Method:  get_grid_face_count[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_face_count"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_face_count(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ int32_t* n_faces,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_face_count) */
    BMI_Model * model = GET_BMI_MODEL(self);
    return model->get_grid_face_count(model->self, grid, n_faces);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_face_count) */
  }
}

/*
 * Method:  get_grid_connectivity[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_connectivity"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_connectivity(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* connectivity,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_connectivity) */
    BMI_Model * model = GET_BMI_MODEL(self);
    int * buffer = sidl_int__array_first(connectivity);

    return model->get_grid_connectivity(model->self, grid, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_connectivity) */
  }
}

/*
 * Method:  get_grid_offset[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_grid_offset"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_grid_offset(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* offset,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_grid_offset) */
    BMI_Model * model = GET_BMI_MODEL(self);
    int * buffer = sidl_int__array_first(offset);

    return model->get_grid_offset(model->self, grid, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_grid_offset) */
  }
}

/*
 * Method:  get_value[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_value"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_value(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* in array<> */ struct sidl__array* dest,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_value) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    char type[2048];
    void * buffer = NULL;

    status = model->get_var_type(model->self, name, type);
    if (status != 0)
      return status;

    if (strcmp(type, "double") == 0) {
      buffer = sidl_double__array_first((struct sidl_double__array*)dest);
    } else if (strcmp(type, "int") == 0) {
      buffer = sidl_int__array_first((struct sidl_int__array*)dest);
    }

    return model->get_value(model->self, name, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.get_value) */
  }
}

/*
 * Method:  get_value_ptr[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_value_ptr"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_value_ptr(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out array<> */ struct sidl__array** values,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_value_ptr) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    char type[2048];
    void * buffer = NULL;
    int size;
    int grid;

    status = model->get_value_ptr(model->self, name, &buffer);
    if (status != 0)
      return status;
    status = model->get_var_type(model->self, name, type);
    if (status != 0)
      return status;
    status = model->get_var_grid(model->self, name, &grid);
    if (status != 0)
      return status;
    status = model->get_grid_size(model->self, grid, &size);
    if (status != 0)
      return status;
    
    {
      const int n_dims = 1;
      const int lower[1] = {0};
      const int upper[1] = {size - 1};
      const int stride[1] = {1};

      if (strcmp(type, "double") == 0) {
        *values = (struct sidl__array*)sidl_double__array_borrow(
            (double*)buffer, n_dims, lower, upper, stride);
      } else if (strcmp(type, "int") == 0) {
        *values = (struct sidl__array*)sidl_int__array_borrow(
            (int*)buffer, n_dims, lower, upper, stride);
      }
    }

    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_value_ptr) */
  }
}

/*
 * Method:  get_value_at_indices[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_get_value_at_indices"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_get_value_at_indices(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* in array<> */ struct sidl__array* dest,
  /* in array<int> */ struct sidl_int__array* inds,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.get_value_at_indices) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    char type[2048];
    void * buffer = NULL;

    status = model->get_var_type(model->self, name, type);
    if (status != 0)
      return status;
    
    if (strcmp(type, "double") == 0) {
      buffer = sidl_double__array_first((struct sidl_double__array*)dest);
    } else if (strcmp(type, "int") == 0) {
      buffer = sidl_int__array_first((struct sidl_int__array*)dest);
    }

    {
      int *inds_start = sidl_int__array_first(inds);
      int len = sidl_int__array_length(inds, 0);

      status = model->get_value_at_indices(model->self, name, buffer, inds_start, len);
    }

    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.get_value_at_indices) */
  }
}

/*
 * Method:  set_value[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_set_value"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_set_value(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* in array<> */ struct sidl__array* values,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.set_value) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    char type[2048];
    void * buffer = NULL;

    status = model->get_var_type(model->self, name, type);
    if (status != 0)
      return status;
    
    if (strcmp(type, "double") == 0) {
      buffer = sidl_double__array_first((struct sidl_double__array*)values);
    } else if (strcmp(type, "int") == 0) {
      buffer = sidl_int__array_first((struct sidl_int__array*)values);
    }

    return model->set_value(model->self, name, buffer);
    /* DO-NOT-DELETE splicer.end(c.Component.set_value) */
  }
}

/*
 * Method:  set_value_at_indices[]
 */

#undef __FUNC__
#define __FUNC__ "impl_c_Component_set_value_at_indices"

#ifdef __cplusplus
extern "C"
#endif
int32_t
impl_c_Component_set_value_at_indices(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* in array<int> */ struct sidl_int__array* inds,
  /* in array<> */ struct sidl__array* src,
  /* out */ sidl_BaseInterface *_ex)
{
  *_ex = 0;
  {
    /* DO-NOT-DELETE splicer.begin(c.Component.set_value_at_indices) */
    int status;
    BMI_Model * model = GET_BMI_MODEL(self);
    char type[2048];
    void * buffer = NULL;

    status = model->get_var_type(model->self, name, type);
    if (status != 0)
      return status;
    
    if (strcmp(type, "double") == 0) {
      buffer = sidl_double__array_first((struct sidl_double__array*)src);
    } else if (strcmp(type, "int") == 0) {
      buffer = sidl_int__array_first((struct sidl_int__array*)src);
    }

    {
      int *inds_start = sidl_int__array_first(inds);
      int len = sidl_int__array_length(inds, 0);

      status = model->set_value_at_indices(model->self, name, inds_start, len, buffer);
    }
    return status;
    /* DO-NOT-DELETE splicer.end(c.Component.set_value_at_indices) */
  }
}
/* Babel internal methods, Users should not edit below this line. */

/* DO-NOT-DELETE splicer.begin(_misc) */
/* Insert-Code-Here {_misc} (miscellaneous code) */
/* DO-NOT-DELETE splicer.end(_misc) */

