// 
// File:          cxx_Component_Impl.hxx
// Symbol:        cxx.Component-v0.0
// Symbol Type:   class
// Babel Version: 1.4.0 (Revision: 6607 release-1-4-0-branch)
// Description:   Server-side implementation for cxx.Component
// 
// WARNING: Automatically generated; only changes within splicers preserved
// 
// 

#ifndef included_cxx_Component_Impl_hxx
#define included_cxx_Component_Impl_hxx

#ifndef included_sidl_cxx_hxx
#include "sidl_cxx.hxx"
#endif
#ifndef included_cxx_Component_IOR_h
#include "cxx_Component_IOR.h"
#endif
#ifndef included_csdms_core_Bmi_hxx
#include "csdms_core_Bmi.hxx"
#endif
#ifndef included_cxx_Component_hxx
#include "cxx_Component.hxx"
#endif
#ifndef included_sidl_BaseClass_hxx
#include "sidl_BaseClass.hxx"
#endif
#ifndef included_sidl_BaseInterface_hxx
#include "sidl_BaseInterface.hxx"
#endif
#ifndef included_sidl_ClassInfo_hxx
#include "sidl_ClassInfo.hxx"
#endif


// DO-NOT-DELETE splicer.begin(cxx.Component._hincludes)
// Insert-Code-Here {cxx.Component._hincludes} (includes or arbitrary code)
${bmi_includes}
${bmi_defines}

#define CALL_BMI_VOID(func,...) { \
  try { \
    state.func(__VA_ARGS__); \
  } catch (int e) { \
    BOCCA_THROW_CXX(::sidl::SIDLException, "Error running " #func); \
  } \
}


#define CALL_BMI(rtn,func,...) { \
  try { \
    rtn = state.func(__VA_ARGS__); \
  } catch (int e) { \
    BOCCA_THROW_CXX(::sidl::SIDLException, "Error running " #func); \
  } \
}

// DO-NOT-DELETE splicer.end(cxx.Component._hincludes)

namespace cxx { 

  /**
   * Symbol "cxx.Component" (version 0.0)
   */
  class Component_impl : public virtual ::cxx::Component 
  // DO-NOT-DELETE splicer.begin(cxx.Component._inherits)
  // Insert-Code-Here {cxx.Component._inherits} (optional inheritance here)
  // DO-NOT-DELETE splicer.end(cxx.Component._inherits)

  {

  // All data marked protected will be accessable by 
  // descendant Impl classes
  protected:

    bool _wrapped;

    // DO-NOT-DELETE splicer.begin(cxx.Component._implementation)
    // Insert-Code-Here {cxx.Component._implementation} (additional details)
    ${bmi_type} state;
    // DO-NOT-DELETE splicer.end(cxx.Component._implementation)

  public:
    // default constructor, used for data wrapping(required)
    Component_impl();
    // sidl constructor (required)
    // Note: alternate Skel constructor doesn't call addref()
    // (fixes bug #275)
      Component_impl( struct cxx_Component__object * ior ) : StubBase(ior,true),
        
    ::csdms::core::Bmi((ior==NULL) ? NULL : &((*ior).d_csdms_core_bmi)) , 
      _wrapped(false) {_ctor();}


    // user defined construction
    void _ctor();

    // virtual destructor (required)
    virtual ~Component_impl() { _dtor(); }

    // user defined destruction
    void _dtor();

    // true if this object was created by a user newing the impl
    inline bool _isWrapped() {return _wrapped;}

    // static class initializer
    static void _load();

  public:


    /**
     *  This function should never be called, but helps babel generate better code. 
     */
    void
    boccaForceUsePortInclude_impl() ;
    /**
     * user defined non-static method.
     */
    bool
    initialize_impl (
      /* in */const ::std::string& config_file
    )
    ;

    /**
     * user defined non-static method.
     */
    bool
    update_impl() ;
    /**
     * user defined non-static method.
     */
    bool
    update_until_impl (
      /* in */double time_interval
    )
    ;

    /**
     * user defined non-static method.
     */
    bool
    finalize_impl() ;
    /**
     * user defined non-static method.
     */
    int32_t
    get_start_time_impl (
      /* out */double& time
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_current_time_impl (
      /* out */double& time
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_end_time_impl (
      /* out */double& time
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_time_step_impl (
      /* out */double& time
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_time_units_impl (
      /* out */::std::string& units
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_component_name_impl (
      /* out */::std::string& name
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_input_item_count_impl (
      /* out */int32_t& count
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_output_item_count_impl (
      /* out */int32_t& count
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_input_var_names_impl (
      /* out array<string> */::sidl::array< ::std::string>& names
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_output_var_names_impl (
      /* out array<string> */::sidl::array< ::std::string>& names
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_var_type_impl (
      /* in */const ::std::string& name,
      /* out */::std::string& type
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_var_units_impl (
      /* in */const ::std::string& name,
      /* out */::std::string& units
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_var_nbytes_impl (
      /* in */const ::std::string& name,
      /* out */int32_t& nbytes
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_var_itemsize_impl (
      /* in */const ::std::string& name,
      /* out */int32_t& size
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_var_grid_impl (
      /* in */const ::std::string& name,
      /* out */int32_t& grid
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_type_impl (
      /* in */int32_t grid,
      /* out */::std::string& type
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_rank_impl (
      /* in */int32_t grid,
      /* out */int32_t& rank
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_size_impl (
      /* in */int32_t grid,
      /* out */int32_t& size
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_shape_impl (
      /* in */int32_t grid,
      /* in array<int> */::sidl::array<int32_t>& shape
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_spacing_impl (
      /* in */int32_t grid,
      /* in array<double> */::sidl::array<double>& spacing
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_origin_impl (
      /* in */int32_t grid,
      /* in array<double> */::sidl::array<double>& origin
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_x_impl (
      /* in */int32_t grid,
      /* in array<double> */::sidl::array<double>& x
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_y_impl (
      /* in */int32_t grid,
      /* in array<double> */::sidl::array<double>& y
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_z_impl (
      /* in */int32_t grid,
      /* in array<double> */::sidl::array<double>& z
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_connectivity_impl (
      /* in */int32_t grid,
      /* in array<int> */::sidl::array<int32_t>& connectivity
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_grid_offset_impl (
      /* in */int32_t grid,
      /* in array<int> */::sidl::array<int32_t>& offset
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_value_impl (
      /* in */const ::std::string& name,
      /* in array<> */::sidl::basearray& dest
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_value_ptr_impl (
      /* in */const ::std::string& name,
      /* out array<> */::sidl::basearray& values
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    get_value_at_indices_impl (
      /* in */const ::std::string& name,
      /* in array<> */::sidl::basearray& dest,
      /* in array<int> */::sidl::array<int32_t>& inds
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    set_value_impl (
      /* in */const ::std::string& name,
      /* in array<> */::sidl::basearray& values
    )
    ;

    /**
     * user defined non-static method.
     */
    int32_t
    set_value_at_indices_impl (
      /* in */const ::std::string& name,
      /* in array<int> */::sidl::array<int32_t>& inds,
      /* in array<> */::sidl::basearray& src
    )
    ;

  };  // end class Component_impl

} // end namespace cxx

// DO-NOT-DELETE splicer.begin(cxx.Component._hmisc)
// Insert-Code-Here {cxx.Component._hmisc} (miscellaneous things)
// DO-NOT-DELETE splicer.end(cxx.Component._hmisc)

#endif
