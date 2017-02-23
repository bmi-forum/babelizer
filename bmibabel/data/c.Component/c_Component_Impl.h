/*
 * File:          c_Component_Impl.h
 * Symbol:        c.Component-v0.0
 * Symbol Type:   class
 * Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
 * Description:   Server-side implementation for c.Component
 * 
 * WARNING: Automatically generated; only changes within splicers preserved
 * 
 */

#ifndef included_c_Component_Impl_h
#define included_c_Component_Impl_h

#ifndef included_sidl_header_h
#include "sidl_header.h"
#endif
#ifndef included_c_Component_h
#include "c_Component.h"
#endif
#ifndef included_csdms_core_Bmi_h
#include "csdms_core_Bmi.h"
#endif
#ifndef included_sidl_BaseClass_h
#include "sidl_BaseClass.h"
#endif
#ifndef included_sidl_BaseInterface_h
#include "sidl_BaseInterface.h"
#endif
#ifndef included_sidl_ClassInfo_h
#include "sidl_ClassInfo.h"
#endif
#ifndef included_sidl_RuntimeException_h
#include "sidl_RuntimeException.h"
#endif
/* DO-NOT-DELETE splicer.begin(c.Component._hincludes) */
/* Insert-Code-Here {c.Component._hincludes} (include files) */
${bmi_includes}

#define _GET_BMI_MODEL(clazz, self) clazz##__get_data(self)->state
#define GET_BMI_MODEL(self) _GET_BMI_MODEL(c_Component, self)
/* DO-NOT-DELETE splicer.end(c.Component._hincludes) */

/*
 * Private data for class c.Component
 */

struct c_Component__data {
  /* DO-NOT-DELETE splicer.begin(c.Component._data) */
  /* Insert-Code-Here {c.Component._data} (private data members) */
  BMI_Model *state;
  /* DO-NOT-DELETE splicer.end(c.Component._data) */
};

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Access functions for class private data and built-in methods
 */

extern struct c_Component__data*
c_Component__get_data(
  c_Component);

extern void
c_Component__set_data(
  c_Component,
  struct c_Component__data*);

extern
void
impl_c_Component__load(
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_c_Component__ctor(
  /* in */ c_Component self,
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_c_Component__ctor2(
  /* in */ c_Component self,
  /* in */ void* private_data,
  /* out */ sidl_BaseInterface *_ex);

extern
void
impl_c_Component__dtor(
  /* in */ c_Component self,
  /* out */ sidl_BaseInterface *_ex);

/*
 * User-defined object methods
 */

#ifdef WITH_RMI
extern struct sidl_BaseInterface__object* 
  impl_c_Component_fconnect_sidl_BaseInterface(const char* url, sidl_bool ar, 
  sidl_BaseInterface *_ex);
#endif /*WITH_RMI*/
extern
void
impl_c_Component_boccaForceUsePortInclude(
  /* in */ c_Component self,
  /* out */ sidl_BaseInterface *_ex);

extern
sidl_bool
impl_c_Component_initialize(
  /* in */ c_Component self,
  /* in */ const char* config_file,
  /* out */ sidl_BaseInterface *_ex);

extern
sidl_bool
impl_c_Component_update(
  /* in */ c_Component self,
  /* in */ double time_interval,
  /* out */ sidl_BaseInterface *_ex);

extern
sidl_bool
impl_c_Component_finalize(
  /* in */ c_Component self,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_start_time(
  /* in */ c_Component self,
  /* out */ double* time,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_current_time(
  /* in */ c_Component self,
  /* out */ double* time,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_end_time(
  /* in */ c_Component self,
  /* out */ double* time,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_component_name(
  /* in */ c_Component self,
  /* out */ char** name,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_input_item_count(
  /* in */ c_Component self,
  /* out */ int32_t* count,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_output_item_count(
  /* in */ c_Component self,
  /* out */ int32_t* count,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_input_var_names(
  /* in */ c_Component self,
  /* in array<string> */ struct sidl_string__array* names,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_output_var_names(
  /* in */ c_Component self,
  /* in array<string> */ struct sidl_string__array* names,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_var_type(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ char** type,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_var_units(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ char** units,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_var_nbytes(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ int32_t* nbytes,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_var_itemsize(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ int32_t* size,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_var_grid(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out */ int32_t* grid,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_type(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ char** type,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_rank(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ int32_t* rank,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_size(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ int32_t* size,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_shape(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* shape,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_spacing(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* spacing,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_origin(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* origin,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_x(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<double> */ struct sidl_double__array* x,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_y(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<double> */ struct sidl_double__array* y,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_z(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<double> */ struct sidl_double__array* z,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_vertex_count(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ int32_t* n_vertices,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_face_count(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* out */ int32_t* n_faces,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_connectivity(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* connectivity,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_grid_offset(
  /* in */ c_Component self,
  /* in */ int32_t grid,
  /* in array<int> */ struct sidl_int__array* offset,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_value(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* in array<> */ struct sidl__array* dest,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_value_ptr(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* out array<> */ struct sidl__array** values,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_get_value_at_indices(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* in array<> */ struct sidl__array* dest,
  /* in array<int> */ struct sidl_int__array* inds,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_set_value(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* in array<> */ struct sidl__array* values,
  /* out */ sidl_BaseInterface *_ex);

extern
int32_t
impl_c_Component_set_value_at_indices(
  /* in */ c_Component self,
  /* in */ const char* name,
  /* in array<int> */ struct sidl_int__array* inds,
  /* in array<> */ struct sidl__array* src,
  /* out */ sidl_BaseInterface *_ex);

#ifdef WITH_RMI
extern struct sidl_BaseInterface__object* 
  impl_c_Component_fconnect_sidl_BaseInterface(const char* url, sidl_bool ar, 
  sidl_BaseInterface *_ex);
#endif /*WITH_RMI*/

/* DO-NOT-DELETE splicer.begin(_hmisc) */
/* Insert-Code-Here {_hmisc} (miscellaneous things) */
/* DO-NOT-DELETE splicer.end(_hmisc) */

#ifdef __cplusplus
}
#endif
#endif
